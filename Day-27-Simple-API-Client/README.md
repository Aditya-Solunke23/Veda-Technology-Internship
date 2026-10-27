# Day 27 – Simple API Client

## Overview
A Python command-line application that calls a public REST API,
retrieves JSON data, and displays selected information in a readable format.

## Features
- Fetches posts from a public REST API
- Allows users to choose how many posts to retrieve
- Processes JSON responses
- Displays post IDs, user IDs, titles, and content
- Checks HTTP response status
- Handles connection errors and request timeouts
- Validates user input

## Technologies Used
- Python 3
- Requests library
- JSON
- JSONPlaceholder REST API

## Project Structure
- `api_client.py` – Main application
- `requirements.txt` – Required Python dependency
- `README.md` – Documentation
- `sample_output.txt` – Example terminal output

## Installation
Install the required library:

```bash
pip install -r requirements.txt