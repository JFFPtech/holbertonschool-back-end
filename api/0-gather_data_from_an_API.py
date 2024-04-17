#!/usr/bin/python3
"""Module to gather data from an API using requests to fetch JSON data."""

import requests
import sys


def get_todo_list_data(employee_id):
    """Retrieve and display todo list data for a given employee ID."""
    base_url = 'https://jsonplaceholder.typicode.com'

    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    if not user_data:
        print(f"No employee record found for ID: {employee_id}")
        return

    todo_params = {'userId': employee_id}
    todo_url = f"{base_url}/todos"
    todo_response = requests.get(todo_url, params=todo_params)
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])
    employee_name = user_data.get('name')

    print(f"Employee {employee_name} completed "
          f"{completed_tasks}/{total_tasks} tasks:")
    for task in todo_data:
        if task['completed']:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        get_todo_list_data(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
