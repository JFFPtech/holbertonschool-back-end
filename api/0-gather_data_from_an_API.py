#!/usr/bin/python3
""" Gather data from an API """

import requests
import sys

employee_id = sys.argv[1]

user_response = requests.get(
    'https://jsonplaceholder.typicode.com/users/' + employee_id)

user_data = user_response.json()

employee_name = user_data['name']

todos_response = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)

todos_data = todos_response.json()

total_todos = str(len(todos_data))

completed_todos = str(sum(1 for task in todos_data if task['completed']))

print('Employee' + employee_name + ' is done with tasks(' + 
        completed_todos + '/' + total_todos + '):')

for task in todos_data:
    if task['completed']:
        print('\t ' + task['title'])

if __name__ == '__main__':
    pass