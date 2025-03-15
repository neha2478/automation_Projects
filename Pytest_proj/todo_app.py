# Here writing a code to create a TO-DO Application

class TodoApp:
    def __init__(self):
        self.tasks = {}
        self.counter = 1

    def add_task(self, task):
        if not task:
            raise ValueError("Task cannot be empty")
        task_id = self.counter
        self.tasks[task_id] = task
        self.counter += 1
        return task_id

    def get_task(self, task_id):
        return self.tasks.get(task_id, None)

    def update_task(self, task_id, new_task):
        if task_id not in self.tasks:
            raise KeyError("Task not found")
        if not new_task:
            raise ValueError("Task cannot be empty")
        self.tasks[task_id] = new_task

    def delete_task(self, task_id):
        if task_id not in self.tasks:
            raise KeyError("Task not found")
        del self.tasks[task_id]

    def list_tasks(self):
        return self.tasks




# class TodoApp:

#     #__init__() constructor
#     def __init__(self):
#         self.tasks = {} #here we are defining a List of Task
#         self.counter = 1 # Defining a counter to keep a count of task

#     #here if we areusing self we are using that reference variable in this function
#     def add_new_Task(self, tasks, counter):
#         if not tasks:
#             raise ValueError("Task cannot be Empty!!")
#         task_id = counter #or we can write self.counter if we don't want to pass it as a parameter
#         self.tasks[task_id] = tasks
#         counter += 1

#         return task_id

#     #To get the task
#     def get_task(self, task_id):
#         return self.tasks.get(task_id, None) # get() to fetch a value .

#     #To update the task
#     def update_task(self, tasks, task_id, new_task):
#         if task_id not in tasks:
#             raise KeyError("Task not Found!!")
#         if not new_task:
#             raise ValueError("Task cannot be Empty!!")
#         self.tasks[task_id] = new_task

#     #To delete a task 
#     def delete_task(self, task_id, tasks):
#         if task_id not in tasks:
#             raise KeyError("Task not found!!")
#         del tasks[task_id]

#     #Return the List of Tasks
#     def list_task(self, tasks):
#         return tasks


    