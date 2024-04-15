#!/usr/bin/python3
""" Gather data from an API """

import csv
import requests
import sys

def get_todo_list_data(employee_id):
    """ Get the todo list data from a given employee id """
    
    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    if not user_data:
        print(f"No employee record found for ID: {employee_id}")
        return
    
    todo_response = requests.get(f"{base_url}/todos", params={'userId': employee_id})
    todo_data = todo_response.json()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        get_todo_list_data(employee_id)
    except ValueError:
        print("Employee ID must be an integer")