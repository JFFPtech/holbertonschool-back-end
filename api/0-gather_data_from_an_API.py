#!/usr/bin/python3
""" Gather data from an API """

import requests
import sys

if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(sys.argv[1])).json()
    
    tasks_done = 0
    total_tasks = 0
    completed_tasks = []
    for task in todo:
        if task['completed']:
            tasks_done += 1
            completed_tasks.append(task['title'])
        total_tasks += 1
    
    print("Employee {} is done with tasks({}/{}):"
            .format(user.get('name'), tasks_done, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))
