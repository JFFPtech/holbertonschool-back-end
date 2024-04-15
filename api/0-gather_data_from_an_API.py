#!/usr/bin/python3
"""Fetch data from the corresponding API"""
import requests
from sys import argv

if __name__ == '__main__':

    user_id = int(argv[1])
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}").json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    

    user_tasks = [task for task in tasks if task['userId'] == user_id]
    completed_tasks = [task for task in user_tasks if task['completed']]
    

    print(f"Employee {user.get('name')} is done with tasks({len(completed_tasks)}/{len(user_tasks)}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")
