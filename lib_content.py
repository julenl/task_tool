#! /usr/bin/env python3
"""
This module defines functions to generate content for the site.
It does not seem very elegant to generate the whole html "content" part
with functions, so I will try to re-implement these funcions as bottle
templates, and probably get rid of this file.
"""

import datetime
from urllib.parse import quote

from definitions import *
from lib_db import *

# Generate an html table with the tasks for the GUI
def html_table(field=None, value=None, statuses=[0,1,2,3]):
    if not statuses or statuses == 'None':
        statuses = [0,1,2,3,4,5]
    items = get_items(field, value)
    fields = task_fields.keys()

    html = []
    html.append('<table class="table">')
    # Header
    html.append('  <thead class="thead-dark">')
    html.append('  <tr>')
    for f in fields:
        html.append('    <th>' +  f + '</th>')
    html.append('  </tr>')
    html.append('  </thead>')
    # Values
    html.append('  <tbody>')
    for item in items:
        html.append('  <tr>')
        if 'status' in item and item['status'] in statuses: 
        #if 'status' in item: 
            for f in fields:
                if f in ['creation', 'start_time', 'finish_time']:
                    try:
                        ts = int(item[f])
                        insert = datetime.datetime.fromtimestamp(ts).strftime('%c')
                    except Exception as e:
                        insert = 'None'
                elif f == 'run_time':
                    try:
                        ts = int(item[f])
                    except Exception as e:
                        ts = 0
                    insert = str(datetime.timedelta(seconds=ts))
                elif f == 'active_periods':
                    if item[f] and item[f] != 'None':
                        ap = [ p for p in item[f].split(',') if p ]
                    else:
                        ap = []
                    #print("AP", ap)
                    insert = str(len(ap))
                elif f == 'status':
                    if item[f] in status:
                        #print("SSS", status[item[f]])
                        status_str = status[item[f]]['label']
                    else:
                        status_str = 'Unknown'
                    insert = status_str.capitalize()
                else:
                    insert = str(item[f])
                html.append('    <td>' +  insert + '</td>')
            #print("ITEM", item)
            html.append('    <td>')
            html.append('      <a href="form?name=' + quote(str(item['name'])) + '">')
            html.append('          <span class="glyphicon glyphicon-pencil"></span>')
            html.append('      </a>')
            html.append('    </td>')
            html.append('    <td>')
            html.append('      <a href="delete?name=' + quote(str(item['name'])) + '">')
            html.append('          <span class="glyphicon glyphicon-trash"></span>')
            html.append('      </a>')
            html.append('    </td>')
            html.append('    </tr>')
            html.append('    </tr>')
    html.append('  <tbody>')

    html.append('</table>')
    html_str = '\n'.join(html)
    return html_str

# Generate an HTML form to create a new task or edit existing one
# to edit a task, pass it's name
def edit_form(name=None):
    prefill = {'name':'','priority':'', 'difficulty':'','description':''}
    if name:
        items = get_items("name", name)
        if len(items) == 1:
            prefill = items[0]

    html = []
    html.append('<form class="form-horizontal" method="POST">')
    for f, values in task_fields.items():
        if not values['auto']:
            html.append('  <div class="form-group">')
            html.append('    <label class="control-label col-sm-4" for="' +
                        f + '">' + values['label'] + ':</label>'
                       )
            html.append('    <div class="col-sm-8">')
            if f in ['name', 'description']:
                html.append('      <input class="form-control" id="' + f +
                            '" name="' + f + '" type="text" value="' +
                            str(prefill[f])+'">'
                           )
            elif f in ['priority', 'difficulty']:
                html.append('      <input class="form-control" id="' + f +
                            '" name="' + f + '" type="text" value="' +
                            str(prefill[f])+'">'
                           )
            html.append('    </div>')
            html.append('  </div>')

    html.append('  <input class="btn btn-default" type="submit" name="Submit" value="Submit">')
    html.append('</form>')

    html_str = '\n'.join(html)
    return html_str


# Create a task-box for the dashboard
# return a list of lines
def create_box(task:dict)->list:
    html = []
    color = ''
    label = status[task['status']]['label']
    bs_color = status[task['status']]['bs_color']
    html.append('<a class="btn btn-info" role="button">')
    html.append('  <div class="bg-' + bs_color + '">')
    html.append('    <h4 style="color: black;">' + task['name'] + '</h4>')
    html.append('    <h5 style="color: black;">' + label + '</h5>')
    html.append('    <form method="post" action="form">')
    html.append('      <input type="hidden" name="name" value="' + task['name'] +'">')
    html.append('      <input type="hidden" name="focus" value="dashboard">')
    epoch = datetime.datetime.now().strftime('%s')
    if task['status'] in [0,2,3,4,5]:
        html.append('      <input type="hidden" name="start_time" value="' + str(epoch) + '">')
        html.append('      <button style="color: black;" type="submit" name="status" value="1">Start</button>')
    else:
        # The task is running
        html.append('      <input type="hidden" name="start_time" value="None">')

        last_dt = int(epoch) - int(task['start_time'])
        time_str = str(datetime.timedelta(seconds=last_dt))
        html.append('      <p style="color: black;">' + time_str + '</p>')

        if not task['run_time'] or task['run_time'] == 'NULL':
            task['run_time'] = "0"
        run_time = int(task['run_time']) + last_dt
        html.append('      <input type="hidden" name="run_time" value="' +str(run_time) + '">')
        if not task['active_periods']:
            task['active_periods'] = ''
        new_chunk = str(task['start_time']) +'-'+ str(epoch)
        active_periods = task['active_periods'].split(',')
        active_periods.append(new_chunk)
        html.append('    <input type="hidden" name="active_periods" value="' +
                    ','.join(active_periods) + '">')

        html.append('      <button style="color: black;" type="submit" name="status" value="2">Stop</button>')
        html.append('      <button style="color: black;" type="submit" name="status" value="4">Finish</button>')
    html.append('    </form>')
    html.append('  </div>')
    html.append('</a>')
    return html


def dashboard_content():
    html = []
    all_tasks = get_items()
    display_status = [1, 0, 2, 3]
    for st in display_status:
        tasks = [item for item in all_tasks if item['status'] == st]
        html.append('<div>')
        html.append('  <h2> Tasks with status "' + status[st]['label'] +
                    '"</h2>')
        for task in tasks:
            # Create click boxes for tasks of type "st"
            html += create_box(task)
        html.append('</div>')

    html_str = '\n'.join(html)
    return html_str

# dashboard_content()
