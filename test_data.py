#! /usr/bin/env python3

"""
Create some test tasks
"""

from lib_db import enter_item

item = {'name': 'test task 1', 'start_time': 1584305015,
        'finish_time': 1584305315, 'run_time': 300,
        'priority': 3, 'difficulty': 4, 'status': 4,
        'description': 'First test task'}
enter_item(item)

item = {'name': 'test task 2', 'start_time': 1584307015,
        'finish_time': 1584307215, 'run_time': 200,
        'priority': 7, 'difficulty': 2, 'status': 4,
        'description': 'Second test task'}
enter_item(item)


item = {'name': 'test task 3', 'start_time': 1584309015,
        'finish_time': 1584309515, 'run_time': 500,
        'priority': 5, 'difficulty': 6, 'status': 4,
        'description': 'Third test task'}
enter_item(item)


item = {'name': 'test task 4', 'start_time': 1584319015,
        'run_time': 500, 'priority': 1, 'difficulty': 5, 'status': 3,
        'description': 'Fourth test task'}
enter_item(item)

item = {'name': 'test task 5', 'start_time': 1584329015,
        'run_time': 800, 'priority': 2, 'difficulty': 8,
        'status': 2, 'description': 'Fifth test task'}
enter_item(item)

item = {'name': 'test task 6', 'start_time': 1584339015,
        'run_time': 700, 'priority': 2, 'difficulty': 3,
        'status': 1, 'description': 'Sixth test task'}
enter_item(item)

item = {'name': 'test task 7', 'start_time': 1584369015,
        'run_time': 100, 'priority': 2, 'difficulty': 3,
        'status': 1, 'description': 'Seventh test task'}
enter_item(item)
