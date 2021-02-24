

tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
# question 1 - done
def find_uncompleted_tasks(tasks_list):
    uncompleted_tasks = []
    for task in tasks_list:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    return uncompleted_tasks

tasks_not_complete = find_uncompleted_tasks(tasks)
print(tasks_not_complete)

#question 2 - probably not as efficient and tidy as it could be

def find_completed_tasks(tasks_list):
    completed_tasks = []
    for task in tasks_list:
        if task["completed"] == True:
            completed_tasks.append(task)
    return completed_tasks

tasks_complete = find_completed_tasks(tasks)
print(tasks_complete)

#task 3 - unable to loop through other results

def task_description(tasks_list):
    for task in tasks_list:
        return task

description_of_task = task_description(tasks)
print(description_of_task["description"])

#task 4 - same issue as #3
def lengthy_tasks(tasks_list):
    longer_tasks = []
    for task in tasks_list:
        if task["time_taken"] > 12:
            longer_tasks.append(task)
    return longer_tasks

all_the_long_tasks = lengthy_tasks(tasks)
print(all_the_long_tasks[0]["description"])

#task 5 BOOM
def task_name_finder(tasks_list, task_description):
    result_name = None
    for task in tasks_list:
        if task["description"] == task_description:
            result_name = task
    return result_name

found_name = task_name_finder(tasks, "Feed Cat")
# print(found_name["description"])


#Task 6


#Task 7 - Done

tasks.append(
    { "description": "Clean the Bog", "completed": False, "time_taken": 100 },
)

print(tasks)