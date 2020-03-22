# Task Tool

Task Tool is a little Bottle app that implements a personal TODO list.

It contains a dashboard in "/" that shows the *active* tasks and buttons to
activate them or put them in *pause* or *completed*.

The *stats* secction generates graphs (currently just one) with statistics
about the tasks. For example, which ones are consuming the most time.

The data is stored in a `sqlite3` database, which is handled by the `lib_db.py`
module. This module can be also used as stand-alone.
