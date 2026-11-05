from datetime import date


class DigitalService:
    def __init__(self, service_id, name, category, description, price, status="Active"):
        self.service_id = service_id
        self.name = name
        self.category = category
        self.description = description
        self.price = price
        self.status = status

    def to_dict(self):
        return {
            "service_id": self.service_id,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "price": self.price,
            "status": self.status
        }


class Program:
    def __init__(self, program_id, name, program_type, duration, seats, status="Upcoming"):
        self.program_id = program_id
        self.name = name
        self.program_type = program_type
        self.duration = duration
        self.seats = seats
        self.status = status

    def to_dict(self):
        return {
            "program_id": self.program_id,
            "name": self.name,
            "program_type": self.program_type,
            "duration": self.duration,
            "seats": self.seats,
            "status": self.status
        }


class CustomerInquiry:
    def __init__(self, inquiry_id, customer_name, email, subject, message, status="Open"):
        self.inquiry_id = inquiry_id
        self.customer_name = customer_name
        self.email = email
        self.subject = subject
        self.message = message
        self.status = status
        self.created_date = str(date.today())

    def to_dict(self):
        return {
            "inquiry_id": self.inquiry_id,
            "customer_name": self.customer_name,
            "email": self.email,
            "subject": self.subject,
            "message": self.message,
            "status": self.status,
            "created_date": self.created_date
        }


class ServiceRequest:
    def __init__(self, request_id, customer_name, service_name, description, priority="Normal", status="Pending"):
        self.request_id = request_id
        self.customer_name = customer_name
        self.service_name = service_name
        self.description = description
        self.priority = priority
        self.status = status
        self.created_date = str(date.today())

    def to_dict(self):
        return {
            "request_id": self.request_id,
            "customer_name": self.customer_name,
            "service_name": self.service_name,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_date": self.created_date
        }