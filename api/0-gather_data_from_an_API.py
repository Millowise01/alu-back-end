#!/usr/bin/python3

import sys
import requests

def get_employee_todo_progress(employee_id):
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print("User not found")
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todos for the user
    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    todos = todos_response.json()

    # Calculate completed tasks
    done_tasks = [todo for todo in todos if todo.get("completed")]
    number_of_done_tasks = len(done_tasks)
    total_number_of_tasks = len(todos)

    # Output the task progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")

    # Print each completed task title
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
