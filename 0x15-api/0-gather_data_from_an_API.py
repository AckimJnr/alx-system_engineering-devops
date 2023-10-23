#!/usr/bin/python3
"""Fetch employee records from an api"""
import json
import requests
import sys


def get_username(userId):
    """Gets the employee username"""
    base_url = "https://jsonplaceholder.typicode.com/"
    url_path = "users/?id={}".format(userId)
    url = base_url + url_path
    result = requests.get(url)
    json_data = result.content.decode('utf-8')
    personal_details = json.loads(json_data)
    employee_name = personal_details[0].get('name')
    return employee_name


def get_tasks(userId):
    """Get the employee tasks"""
    base_url = "https://jsonplaceholder.typicode.com/"
    url_path = "todos/?userId={}".format(userId)
    url = base_url + url_path
    result = requests.get(url)
    json_data = result.content.decode('utf-8')
    employee_tasks = json.loads(json_data)
    return employee_tasks


if __name__ == '__main__':
    """execute as a main program only"""
    completed = 0

    if (len(sys.argv) > 0):
        userId = sys.argv[1]
        employee_name = get_username(userId)
        employee_tasks = get_tasks(userId)
        total_tasks = len(employee_tasks)
        for task in employee_tasks:
            if task.get('completed'):
                completed += 1
        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, completed, total_tasks))

        for task in employee_tasks:
            if task.get('completed'):
                print('\t ' + task.get('title'))
