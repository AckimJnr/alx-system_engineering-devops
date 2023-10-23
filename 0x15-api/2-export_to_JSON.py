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
    username = personal_details[0].get('username')
    return username


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
    if len(sys.argv) < 2:
        print("Usage: python script.py USER_ID")
        sys.exit(1)

    user_id = sys.argv[1]
    file_name = f"{user_id}.json"
    username = get_username(user_id)
    employee_tasks = get_tasks(user_id)
    total_tasks = len(employee_tasks)

    employee_list = []

    for task in employee_tasks:
        employee_list.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    employee_dictionary = {user_id: employee_list}

    employee_information = json.dumps(employee_dictionary)

    with open(file_name, "w") as emp_data:
        emp_data.write(employee_information)
