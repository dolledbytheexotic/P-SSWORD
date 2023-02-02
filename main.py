from dolist import tasks
TASK=tasks

optional_task=[]


def to_do(task):
     optional_task.append(task)

for task in TASK:
    to_do(task)

def do():
    print("To do list: ")
    for i, task in enumerate(tasks):
        print(i + 1, task)

if optional_task:
    do()
else:
    print("The task list is empty")
