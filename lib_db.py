#! /usr/bin/env python3
"""
This module implements three main functions to interact with a sqlite3
database:
- ensure_table: if the database file or the table, with the given layout, do
  exist, it creates them
- enter_item: to insert a new item (task) into the database or edit an existing
  one
- get_items" get all the items in the database, or just the ones with a
  given field:value

The interactive mode implements these two last options as 'enter' and 'get'.

The layout of the task items is described in the "task_fields" dictionary,
where the keys are the fields and the values, the SQL data type.
"""
import os
import sys
import json
import sqlite3
import datetime

from definitions import *

username = 'default'
db_dir = os.getcwd() + '/dbs'
db_file = db_dir + '/' + username + '.db'
if not os.path.isdir(db_dir):
    os.makedirs(db_dir)

# Ensure that the database exists and the table is created
def ensure_table():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    # Create a big string with all fields and types, as:
    # "name text, creation_date integer, start_time integer, ..."
    fields = ', '.join(
                      [k + ' ' + v['sql_type'] for k, v in task_fields.items()]
                      )
    sql = 'CREATE TABLE IF NOT EXISTS tasks (' + fields + ')'
    c.execute(sql)
    conn.commit()
    conn.close()


ensure_table()


def sql_run(sql):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute(sql)
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

# Insert a new item
def new_item(item:dict):
    fields_str = ', '.join(task_fields.keys())
    values = []
    for f in task_fields.keys():
        if f in item:
            values.append('"' + str(item[f]) + '"')
        elif f == 'creation':
            epoch = datetime.datetime.now().strftime('%s')
            values.append('"' + str(epoch) + '"')
        elif f == 'priority':
            values.append("0")
        elif f == 'difficulty':
            values.append("0")
        elif f == 'status':
            values.append("0")
        elif f == 'run_type':
            values.append("0")
        elif f == 'active_periods':
            values.append("NULL")
        else:
            values.append('NULL')
    values_str = ', '.join(values)
    sql = 'INSERT INTO tasks (' + fields_str + ') VALUES(' + values_str + ');'
    sql_run(sql)

# Update an existing item
def update_item(name, fields:dict):
    values = []
    for f in task_fields.keys():
        if f in fields:
            values.append( f + '="' + str(fields[f]) + '"')
    values_str = ', '.join(values)
    sql = 'UPDATE tasks SET ' + values_str + ' WHERE name="' + name + '";'
    sql_run(sql)

# Insert or update item, depending on if it already exists or not
def enter_item(item:dict):
    if 'name' in item:
        sql = 'SELECT * from tasks WHERE name="' + item['name'] + '";'
        res = sql_run(sql)
    else:
        print('ERROR: no task "name" provided')
        return
    if len(res) == 0:
        new_item(item)
    elif len(res) == 1:
        name = item.pop('name')
        update_item(name, item)


def delete_item(name):
    # Check that the element exists before trying to delete it
    sql = 'SELECT * from tasks WHERE name="' + name + '";'
    res = sql_run(sql)
    if len(res) == 1:
        sql = 'DELETE FROM tasks WHERE name="' + name + '";'
        sql_run(sql)


# Take a list of raw tasks from the database and return it solved
# Because we want to show human readable stuff on the HTML instead of i.e.
# EPOCH timestamps or numeric statuses
def human_readable(tasks:list)->list:
    output = []
    for task in tasks:
        for k,v in task.items():
            if k in ['creation', 'start_time', 'finish_time']:
                try:
                    ts = int(task[k])
                    t = datetime.datetime.fromtimestamp(ts).strftime('%c')
                except Exception as e:
                    t = 'None'
                task[k] = t

            elif k == 'run_time':
                try:
                    ts = int(task[k])
                except Exception as e:
                    ts = 0
                task[k] = str(datetime.timedelta(seconds=ts))
            elif k == 'active_periods':
                if task[k] and task[k] != 'None':
                    ap = [p for p in task[k].split(',') if p ]
                else:
                    ap = []
                task[k] = str(len(ap))
            elif k == 'status':
                if task[k] in status:
                    status_str = status[task[k]]['label']
                else:
                    status_str = 'Unknown'
                task[k] = status_str.capitalize()
            else:
                task[k] = str(task[k])
        output.append(task)
    return output

 

# Get items from database as a list of dictionaries
# Optionally use "field" and "value" for filtering
def get_items(field=None, value=None, statuses=None, printable=False)->list:
    where = ''
    if field:
        where = ' WHERE ' + field + '="' + value + '"'

    sql = 'SELECT * from tasks ' + where + ';'
    res = sql_run(sql)
    fields = task_fields.keys()
    output = []
    for r in res:
        tmp = dict(zip(fields, r))
        output.append(tmp)

    if statuses and isinstance(statuses, list):
        output = [task for task in output if item['status'] in statuses]
    if printable:
        output = human_readable(output)

    return output


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('action', type=str, choices=['enter', 'get'],
                        help='Enter value to DB or retrieve from DB')
    parser.add_argument('-d', '--data', type=str, help='Data to enter')
    parser.add_argument('--field', type=str, help='Field to filter')
    parser.add_argument('--value', type=str, help='Value to filter')
    args = parser.parse_args()

    if args.action == 'enter':
        if not args.data:
            print('ERROR: you must provide valid data with the flag "-d"')
            sys.exit(1)
        try:
            data = json.loads(args.data)
        except exception as e:
            print('ERROR: invalid JSON')
            sys.exit()
        enter_item(data)
    elif args.action == 'get':
        print(json.dumps(get_items(args.field, args.value), indent=4))
