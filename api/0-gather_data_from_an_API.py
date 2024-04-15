#!/usr/bin/python3
""" Gather data from an API """

import requests
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]

    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user_data = user_response.json()

    if not user_data:
        print(f'No employee record found for ID: {employee_id}')
        sys.exit(1)

    employee_name = user_data['name']

    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos_data = todos_response.json()

    total_todos = len(todos_data)
    completed_todos = sum(task['completed'] for task in todos_data)

    print(f'Employee {employee_name} is done with tasks({completed_todos}/{total_todos}):')

    for task in todos_data:
        if task['completed']:
            print(f'\t {task["title"]}')

if __name__ == '__main__':
    main()
