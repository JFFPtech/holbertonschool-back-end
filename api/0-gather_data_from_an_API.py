#!/usr/bin/python3
"""Fetch data from the corresponding API"""
import requests
from sys import argv

if __name__ == '__main__':
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(int(argv[1]))).json()
    completed_tasks = [i for i in tasks if i.get('completed') and
                       i.get('userId') == int(argv[1])]
    total_tasks = len([i for i in tasks if i['userId'] == int(argv[1])])
    print("Employee {} is done with tasks({}/{}):"
          .format(str(user.get('name')), len(completed_tasks), total_tasks))
    for i in completed_tasks:
        print("\t {}".format(i.get('title')))