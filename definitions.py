#! /usr/bin/env python3
"""
This file contains variable and parameter definitions for the task-tool
"""

# Dict with field names with their sql data type, python data type,
# display label and whether they are automatically generated
task_fields = {}
task_fields['name'] = {
                       'sql_type': 'TEXT PRIMARY KEY',
                       'p_type': str,
                       'label': 'Name of the task',
                       'auto': False
                      }
task_fields['creation'] = {
                           'sql_type': 'INTEGER',
                           'p_type': int,
                           'label': 'Task creation time',
                           'auto': True
                          }
task_fields['start_time'] = {
                             'sql_type': 'INTEGER',
                             'p_type': int,
                             'label': 'Time the task started',
                             'auto': True
                            }
task_fields['finish_time'] = {
                              'sql_type': 'INTEGER',
                              'p_type': int,
                              'label': 'Time the task was completed',
                              'auto': True
                             }
task_fields['priority'] = {
                           'sql_type': 'INTEGER',
                           'p_type': int,
                           'label': 'Task priority from 0 (min) to 10 (max)',
                           'auto': False
                           }

task_fields['difficulty'] = {
                          'sql_type': 'INTEGER',
                          'p_type': int,
                          'label': 'Task difficulty from 0 (min) to 10 (max)',
                          'auto': False
                          }
task_fields['run_time'] = {
                           'sql_type': 'INTEGER',
                           'p_type': int,
                           'label': 'Total time the task has been running',
                           'auto': True
                           }
task_fields['active_periods'] = {
                             'sql_type': 'TEXT',
                             'p_type': str,
                             'label': 'Time periods the task has been running',
                             'auto': True
                             }
task_fields['status'] = {
                         'sql_type': 'INTEGER',
                         'p_type': int,
                         'label': 'Current status of the task',
                         'auto': True
                         }
task_fields['tags'] = {
                       'sql_type': 'TEXT',
                       'p_type': str,
                       'label': 'List of classification tags',
                       'auto': False
                       }
task_fields['description'] = {
                              'sql_type': 'TEXT',
                              'p_type': str,
                              'label': 'Detailed description of the task',
                              'auto': False
                              }

# Map status numbers to actual words
status = {}
status[0] = {'label': 'new', 'bs_color': 'primary'}
status[1] = {'label': 'running', 'bs_color': 'success'}
status[2] = {'label': 'paused', 'bs_color': 'muted'}
status[3] = {'label': 'waiting', 'bs_color': 'warning'}
status[4] = {'label': 'completed', 'bs_color': 'info'}
status[5] = {'label': 'unknown', 'bs_color': 'dark'}
