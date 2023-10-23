#!/usr/bin/python3
"""Fetch and export all employee tasks in JSON format"""
import json
import requests


def get_username(userId):
    """Gets the employee username"""
    base_url = "https://jsonplaceholder.typicode.com/"
    url_path = f"users/{userId}"
    url = base_url + url_path
    result = requests.get(url)
    personal_details = result.json()
    username = personal_details.get('username')
    return username


def get_all_employee_tasks():
    """Get all employee tasks"""
    base_url = "https://jsonplaceholder.typicode.com/"
    url_path = "todos"
    url = base_url + url_path
    result = requests.get(url)
    employee_tasks = result.json()
    return employee_tasks


if __name__ == '__main__':
    """Begin program execution"""
    employee_tasks = get_all_employee_tasks()
    employee_data = {}

    for task in employee_tasks:
        user_id = task.get('userId')
        username = get_username(user_id)

        task_info = {
            "username": username,
            "task": task.get('title'),
            "completed": task.get('completed')
        }

        if user_id in employee_data:
            employee_data[user_id].append(task_info)
        else:
            employee_data[user_id] = [task_info]
    with open("todo_all_employees.json", "w") as emp_data:
        emp_data.write(json.dumps(employee_data))
