# here the Pytest Test Suite

import pytest

from pathlib import Path

# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from todo_app import TodoApp  # Assuming the above TodoApp is saved in `todo_app.py`

pythonFile = 'todo_app.py'
pythonFileDir = 'src'

BASE_DIR = Path(__file__).resolve().parent
DATA_File = BASE_DIR.joinpath(pythonFileDir).joinpath(pythonFile)

@pytest.fixture
def todo_app():
    """Fixture to create a fresh TodoApp instance for each test."""
    return TodoApp()

def test_add_task(todo_app):
    task_id = todo_app.add_task("Buy groceries")
    assert task_id == 1
    assert todo_app.get_task(task_id) == "Buy groceries"

def test_add_empty_task(todo_app):
    with pytest.raises(ValueError, match="Task cannot be empty"):
        todo_app.add_task("")

def test_get_task(todo_app):
    task_id = todo_app.add_task("Read a book")
    assert todo_app.get_task(task_id) == "Read a book"
    assert todo_app.get_task(999) is None

def test_update_task(todo_app):
    task_id = todo_app.add_task("Wash the car")
    todo_app.update_task(task_id, "Wash the bike")
    assert todo_app.get_task(task_id) == "Wash the bike"

def test_update_non_existent_task(todo_app):
    with pytest.raises(KeyError, match="Task not found"):
        todo_app.update_task(999, "New Task")

def test_update_with_empty_task(todo_app):
    task_id = todo_app.add_task("Clean the house")
    with pytest.raises(ValueError, match="Task cannot be empty"):
        todo_app.update_task(task_id, "")

def test_delete_task(todo_app):
    task_id = todo_app.add_task("Go jogging")
    todo_app.delete_task(task_id)
    assert todo_app.get_task(task_id) is None

def test_delete_non_existent_task(todo_app):
    with pytest.raises(KeyError, match="Task not found"):
        todo_app.delete_task(999)

def test_list_tasks(todo_app):
    todo_app.add_task("Task 1")
    todo_app.add_task("Task 2")
    tasks = todo_app.list_tasks()
    assert len(tasks) == 2
    assert tasks[1] == "Task 1"
    assert tasks[2] == "Task 2"
