import json

def filter_raw_task_data(data):
    result = ''
    tasks = json.loads(data)
    for task in tasks:
        result += task['name'] + '\n'
    return result 
