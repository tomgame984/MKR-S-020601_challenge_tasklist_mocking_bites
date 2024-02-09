from lib.task_list import TaskList
from unittest.mock import Mock


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

"""
Mock test:
Add a mock task
append mock task to tasks list
"""
def test_mock_task_created_and_added_to_list():
    task_list = TaskList()
    mock_task = Mock()
    task_list.add(mock_task)
    assert task_list.tasks == [mock_task]

"""
Mock test:
Add multiple mock tasks to tasks list 
return list of all tasks
"""

def test_mock_multiple_tasks_added_and_return_all_tasks_list():
    task_list = TaskList()
    mock_task_1 = Mock()
    mock_task_2 = Mock()
    mock_task_3 = Mock()
    task_list.add(mock_task_1)
    task_list.add(mock_task_2)
    task_list.add(mock_task_3)
    assert task_list.all() == [mock_task_1, mock_task_2, mock_task_3]

"""
Mock test:
Add multiple mock tasks to tasks list
Marks mock tasks as complete
Return all complete as True
"""
def test_mock_all_tasks_complete_and_return_True():
    task_list = TaskList()
    mock_task_1 = Mock()
    mock_task_1.is_complete.return_value = True
    task_list.add(mock_task_1)
    mock_task_2 = Mock()
    mock_task_2.is_complete.return_value = True
    task_list.add(mock_task_2)
    mock_task_3 = Mock()
    mock_task_3.is_complete.return_value = True    
    task_list.add(mock_task_3)
    assert task_list.all_complete() == True


"""
Mock test:
Add multiple mock tasks to tasks list
Marks some mock tasks as complete
Return all complete as False
"""
def test_mock_not_all_tasks_complete_and_return_False():
    task_list = TaskList()
    mock_task_1 = Mock()
    mock_task_1.is_complete.return_value = True
    task_list.add(mock_task_1)
    mock_task_2 = Mock()
    mock_task_2.is_complete.return_value = False
    task_list.add(mock_task_2)
    mock_task_3 = Mock()
    mock_task_3.is_complete.return_value = True    
    task_list.add(mock_task_3)
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour
