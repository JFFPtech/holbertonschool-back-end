#!/bin/usr/python3
""" Gather data from an API """

import requests
import sys

def get_todo_list_data(employee_id):
    """ Get the todo list data from a given employee id """
    
    base_url = 'https://jsonplaceholder.typicode.com'
    user_respone = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_respone.json()