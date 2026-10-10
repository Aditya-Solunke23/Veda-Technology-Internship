# Day 10 - Contact Book Using Dictionaries

## Project Description

This project is a command-line Contact Book application built using Python dictionaries.

The application allows users to add, view, search, update, and delete contact information through a menu-driven interface.

## Objective

The objective of this task is to learn dictionaries and practical key-value data management.

## Features

- Add contacts
- View all contacts
- Search for a contact
- Update contact information
- Delete contacts
- Prevent duplicate contact IDs
- Validate user input
- Menu-driven command-line interface

## Data Structure

A Python dictionary is used to store the contacts.

Each contact ID acts as a key, while the contact information is stored as a dictionary value.

Example:

```python
contacts = {
    "C001": {
        "name": "Aditya",
        "phone": "9876543210",
        "email": "aditya@example.com"
    }
}