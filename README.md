Gtimelog
========

Gtimelog fork with improved importing of tasks

New setting `task_list_filter` has been added, it should contain a module name with implementation of filtering logic.
The module should contain only one function: `filter_raw_tasks_data(data)`

`dummy.py` and `trello.py` are examples of such modules
