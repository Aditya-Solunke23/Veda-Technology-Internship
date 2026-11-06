from storage import load_data


def search_all_records():
    """Search across services, programs, inquiries, and service requests."""

    keyword = input("Enter keyword to search: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    services = load_data("services.json")
    programs = load_data("programs.json")
    inquiries = load_data("inquiries.json")
    requests = load_data("requests.json")

    results = []

    # Search digital services
    for service in services:
        searchable_text = (
            service["name"] + " " +
            service["category"] + " " +
            service["description"] + " " +
            service["status"]
        ).lower()

        if keyword in searchable_text:
            results.append(
                f"[Service] {service['service_id']} - "
                f"{service['name']} - {service['status']}"
            )

    # Search programs
    for program in programs:
        searchable_text = (
            program["name"] + " " +
            program["program_type"] + " " +
            program["duration"] + " " +
            program["status"]
        ).lower()

        if keyword in searchable_text:
            results.append(
                f"[Program] {program['program_id']} - "
                f"{program['name']} - {program['status']}"
            )

    # Search customer inquiries
    for inquiry in inquiries:
        searchable_text = (
            inquiry["customer_name"] + " " +
            inquiry["subject"] + " " +
            inquiry["message"] + " " +
            inquiry["status"]
        ).lower()

        if keyword in searchable_text:
            results.append(
                f"[Inquiry] {inquiry['inquiry_id']} - "
                f"{inquiry['customer_name']} - {inquiry['status']}"
            )

    # Search service requests
    for request in requests:
        searchable_text = (
            request["customer_name"] + " " +
            request["service_name"] + " " +
            request["description"] + " " +
            request["priority"] + " " +
            request["status"]
        ).lower()

        if keyword in searchable_text:
            results.append(
                f"[Request] {request['request_id']} - "
                f"{request['customer_name']} - "
                f"{request['status']}"
            )

    print("\n========== SEARCH RESULTS ==========")

    if not results:
        print("No matching records found.")
    else:
        for result in results:
            print(result)

    print("===================================")