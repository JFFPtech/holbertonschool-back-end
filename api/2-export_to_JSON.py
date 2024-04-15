#!/usr/bin/python3
""" Gather data from an API and export to JSON"""

import json
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

    user_tasks = []
    for task in todo_data:
        user_tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_data.get('username')
        })