#!/usr/bin/python3
"""Script to gather TODO list progress of an employee from a REST API"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """Fetch and display TODO progress for a given employee ID."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_info = requests.get(url).json()
    todo_info = requests.get(todo_url).json()

    employee_name = user_info.get("name")
    total_tasks = list(filter(lambda x: x.get("completed") is True, todo_info))
    task_com = len(total_tasks)
    total_task_done = len(todo_info)

    print(f"Employee {employee_name} is done with tasks({task_com}/{total_task_done}):")

    [print(f"\t {task.get('title')}") for task in total_tasks]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
        sys.exit(1)
