# Task Tool

Task Tool is a little Bottle app that implements a personal TODO list.

It contains a dashboard in "/" that shows the *active* tasks and buttons to
activate them or put them in *pause* or *completed*.

The *stats* secction generates graphs (currently just one) with statistics
about the tasks. For example, which ones are consuming the most time.

The data is stored in a `sqlite3` database, which is handled by the `lib_db.py`
module. This module can be also used as stand-alone.


## Quick Start

You need to have Python3 installed in your system and the following modules:

- bottle
- sqlite3
- mathplotlib

If you don't, install them with

    pip install bottle
    pip install sqlite3
    pip install mathplotlib

> If you are on GNU/Linux, you may have to use `pip3` instead of `pip`.

- Download the [ZIP file](https://github.com/julenl/task_tool/archive/master.zip)

- Get into the `task_tool-master` directory and execute the app either by double clicking or even better, from a Terminal with:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ {.bash}
python app.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Now open a web browser and go to (http://localhost:8080). You should find the main site. It does not contain any data, so you can just load some test data to get a feeling of how it looks. Just click on the "*Click here to add some*" (test data) and you will have something to look at.
Or, of course, you can also create your own tasks...


