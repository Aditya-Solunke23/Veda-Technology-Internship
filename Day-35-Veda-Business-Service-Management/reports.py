from storage import load_data


def view_business_report():
    """Display a summary of business records."""

    services = load_data("services.json")
    programs = load_data("programs.json")
    inquiries = load_data("inquiries.json")
    requests = load_data("requests.json")

    # Digital services
    active_services = sum(
        1 for service in services
        if service["status"].lower() == "active"
    )

    # Program categories
    technology_programs = sum(
        1 for program in programs
        if program["program_type"].lower() == "technology"
    )

    training_programs = sum(
        1 for program in programs
        if program["program_type"].lower() == "training"
    )

    internship_programs = sum(
        1 for program in programs
        if program["program_type"].lower() == "internship"
    )

    # Customer inquiries
    open_inquiries = sum(
        1 for inquiry in inquiries
        if inquiry["status"].lower() == "open"
    )

    resolved_inquiries = sum(
        1 for inquiry in inquiries
        if inquiry["status"].lower() == "resolved"
    )

    # Service requests
    pending_requests = sum(
        1 for request in requests
        if request["status"].lower() == "pending"
    )

    completed_requests = sum(
        1 for request in requests
        if request["status"].lower() == "completed"
    )

    urgent_requests = sum(
        1 for request in requests
        if request["priority"].lower() == "urgent"
    )

    print("\n==========================================")
    print("       VEDA TECHNOLOGY BUSINESS REPORT")
    print("==========================================")

    print("\nDIGITAL SERVICES")
    print(f"Total Services       : {len(services)}")
    print(f"Active Services      : {active_services}")

    print("\nPROGRAMS")
    print(f"Technology Programs  : {technology_programs}")
    print(f"Training Programs    : {training_programs}")
    print(f"Internship Programs  : {internship_programs}")
    print(f"Total Programs       : {len(programs)}")

    print("\nCUSTOMER INQUIRIES")
    print(f"Total Inquiries      : {len(inquiries)}")
    print(f"Open Inquiries       : {open_inquiries}")
    print(f"Resolved Inquiries   : {resolved_inquiries}")

    print("\nSERVICE REQUESTS")
    print(f"Total Requests       : {len(requests)}")
    print(f"Pending Requests     : {pending_requests}")
    print(f"Completed Requests   : {completed_requests}")
    print(f"Urgent Requests      : {urgent_requests}")

    print("\n==========================================")