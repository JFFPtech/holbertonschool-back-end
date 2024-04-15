#!/usr/bin/python3
""" Gather data from an API and export it to a JSON file """

import requests
import sys
import json

def export_todo_list_to_json(employee_id):
    """ Fetches todo list for a given employee and exports it to a JSON file """
    
    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    if not user_data:
        print(f"No employee record found for ID: {employee_id}")
        return

    todo_response = requests.get(f"{base_url}/todos", params={'userId': employee_id})
    todo_data = todo_response.json()

    user_tasks = []
    for task in todo_data:
        user_tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user_data['username']
        })

    json_data = {
        str(employee_id): user_tasks
    }

    json_file_name = f"{employee_id}.json"

    with open(json_file_name, 'w') as file:
        json.dump(json_data, file, indent=4)

    print(f"Data exported to {json_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        export_todo_list_to_json(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
