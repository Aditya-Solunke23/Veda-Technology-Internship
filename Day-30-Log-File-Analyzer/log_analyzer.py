"""
Day 30 - Log File Analyzer
Analyzes server logs to summarize requests, errors,
frequent IP addresses, and commonly requested endpoints.
"""

import re
from collections import Counter
from pathlib import Path


LOG_FILE = Path(__file__).parent / "sample_server.log"


def parse_log_line(line):
    """Extract the IP address, endpoint, and HTTP status code."""
    pattern = (
        r'^(\S+)\s+\S+\s+\S+\s+'
        r'\[[^\]]+\]\s+'
        r'"([A-Z]+)\s+(\S+)\s+[^"]+"\s+'
        r'(\d{3})\s+\S+'
    )

    match = re.search(pattern, line)

    if not match:
        return None

    ip_address, method, endpoint, status_code = match.groups()

    return {
        "ip": ip_address,
        "method": method,
        "endpoint": endpoint,
        "status": int(status_code),
    }


def read_logs(file_path):
    """Read and parse valid log entries from a file."""
    records = []
    malformed_lines = 0

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                record = parse_log_line(line.strip())

                if record is None:
                    malformed_lines += 1
                    continue

                records.append(record)

    except FileNotFoundError:
        print(f"Error: Log file not found: {file_path}")
        return None, 0

    except OSError as error:
        print(f"Error reading log file: {error}")
        return None, 0

    return records, malformed_lines


def analyze_logs(records):
    """Calculate request statistics from parsed log entries."""
    ip_counts = Counter(record["ip"] for record in records)
    endpoint_counts = Counter(
        record["endpoint"] for record in records
    )
    status_counts = Counter(
        record["status"] for record in records
    )

    error_count = sum(
        1 for record in records
        if 400 <= record["status"] <= 599
    )

    return {
        "total_requests": len(records),
        "error_count": error_count,
        "ip_counts": ip_counts,
        "endpoint_counts": endpoint_counts,
        "status_counts": status_counts,
    }


def display_report(report, malformed_lines):
    """Print the log analysis report."""
    print("\n" + "=" * 55)
    print("                 LOG ANALYSIS REPORT")
    print("=" * 55)

    print(f"Total requests       : {report['total_requests']}")
    print(f"Error responses (4xx/5xx): {report['error_count']}")
    print(f"Malformed lines      : {malformed_lines}")

    print("\nHTTP STATUS CODE SUMMARY")
    print("-" * 55)

    for status, count in sorted(report["status_counts"].items()):
        print(f"HTTP {status}: {count}")

    print("\nTOP 5 IP ADDRESSES")
    print("-" * 55)

    for ip, count in report["ip_counts"].most_common(5):
        print(f"{ip:<25} {count} request(s)")

    print("\nTOP 5 REQUESTED ENDPOINTS")
    print("-" * 55)

    for endpoint, count in report["endpoint_counts"].most_common(5):
        print(f"{endpoint:<35} {count} request(s)")

    print("=" * 55)


def main():
    """Run the log file analyzer."""
    print("=" * 55)
    print("                 LOG FILE ANALYZER")
    print("=" * 55)

    records, malformed_lines = read_logs(LOG_FILE)

    if records is None:
        return

    if not records:
        print("No valid log entries were found.")
        print(f"Malformed lines: {malformed_lines}")
        return

    report = analyze_logs(records)
    display_report(report, malformed_lines)


if __name__ == "__main__":
    main()