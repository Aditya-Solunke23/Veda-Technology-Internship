# Day 30 – Log File Analyzer

## Overview
A Python application that analyzes server log files and generates
a summary of requests, HTTP errors, frequent IP addresses,
and commonly requested endpoints.

## Features
- Reads server log files
- Extracts IP addresses, endpoints, methods, and status codes
- Counts total requests
- Identifies HTTP 4xx and 5xx responses
- Lists the most frequent IP addresses
- Lists the most requested endpoints
- Summarizes HTTP status codes
- Handles malformed log entries
- Reports file access errors

## Technologies Used
- Python 3
- Regular expressions (`re`)
- Counter from `collections`
- File handling with `pathlib`

## Installation
No external dependencies are required.

## How to Run
Place `sample_server.log` in the same directory as `log_analyzer.py`.

Run:

```bash
python log_analyzer.py