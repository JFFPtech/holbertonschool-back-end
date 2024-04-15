#!/usr/bin/python3
""" Gather data from an API and export it to a JSON file """

import json
import requests

def fetch_all_tasks():
    """ Fetches all tasks for all employees and exports to JSON """
    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f"{base_url}/users")
    user_data = user_response.json()

    all_tasks = {}

    for user in user_data:
        user_id = user['id']
        username = user['username']

        todo_response = requests.get(f"{base_url}/todos", params={'userId': user_id})
        todo_data = todo_response.json()

        user_tasks = []
        for task in todo_data:
            user_tasks.append({
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            })

        all_tasks[str(user_id)] = user_tasks