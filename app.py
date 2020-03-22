#! /usr/bin/env python3

from bottle import run, template, route, request, static_file, redirect

import lib_db
import lib_content
import lib_stats


@route('/imgs/<filename>')
def server_static(filename):
    return static_file(filename, root='imgs/')


@route('/')
def main():
    content = lib_content.dashboard_content()
    print("CONTENT", content)
    return template('bulk', content=content)



@route('/tasks')
@route('/tasks', method="GET")
def list():
    opts = dict(request.query.decode())
    fields = ['field', 'value', 'statuses']
    pass_fields = {'printable': True}
    for k, v in opts.items():
        if k in fields:
            pass_fields[k] = v
    tasks = lib_db.get_items(**pass_fields)
    content = ''
    return template('bulk', content=content, tasks=tasks)


# Form to add/edit tasks
# If GET contains 'name' and a task with that name exists, edit it
# If we have POST, create/update the task
@route('/form')
@route('/form', method=["GET", "POST"])
def list():
    getopts = dict(request.query.decode())
    # print("GET", getopts)
    task_name = None
    if 'test_tasks' in getopts:
        import test_data

    elif 'name' in getopts:
        task_name = getopts['name']

    # If we have valid POST, process and return to dashboard
    postopts = dict(request.POST.decode())
    if 'name' in postopts:
        lib_db.enter_item(postopts)
        if 'focus' in postopts and postopts['focus'] == 'dashboard':
            redirect('/')
        else:
            redirect('/tasks')

    content = lib_content.edit_form(task_name)
    return template('bulk', content=content)


@route('/stats')
@route('/stats', method="GET")
def stats():
    stats = {}
    stats['run_times'] = lib_stats.stat_run_time()
    return template('bulk', stats=stats)


@route('/delete', method="GET")
def delete():
    getopts = dict(request.query.decode())
    if 'name' in getopts:
        lib_db.delete_item(getopts['name'])
    redirect('/tasks')


if __name__ in "__main__":
    run(host='localhost', port=8080, debug=True, reloader=True)
