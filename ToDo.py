class Task:
     #constructor method
     def __init__(self, name, description, category, priority, status):
          self.name = name
          self.description = description
          self.category = category
          self.priority = priority
          self.status = status
    #function to make the attribute human redable 
    # f to write python expression between curly braces to have resulting value
     def __str__(self):
          return (f'name: {self.name}\ndescription: {self.description}'
                  f'\ncategory:{self.category}\npriority:{self.priority}\nstatus:{self.status}')     

tasks = []

def show_menu():
        print('\n=== To_Do_List ===')
        print('1. Add task')
        print('2. Edit task')
        print('3. View To_Do_List')
        print('4. Delete task')
        print('5. edit task status')
        print('6. ascending order')
        print('7. descending order')
        print('8. Exit')

#To add tasks to To_do_list:
def add_task():
            
     name = input('Enter the task name: ')
     description = input('Enter the task description: ')
     category = input('Enter the task category: ')
     priority = input('Enter the task priority(low or medium or high): ')
     status = input('Enter the task status (to_do or done or canceled): ')

     new_task = Task(name, description, category, priority, status)
     tasks.append(new_task)
     print('Task added!')

#Edit any task you choose
def edit_task():
    if len(tasks) == 0:
        print('No tasks to edit')
        return
    view_list()
    task_num = int(input('number of task you want to edit: '))
    if   task_num <= len(tasks):
         task = tasks[task_num-1]
         print('edit the task')
         print(task)
         task.name = input('enter the new name: ')
         task.description = input('enter the new description: ')
         task.category = input('enter the new category: ')
         task.priority = input('enter the new priority: ')
         task.status = input('enter the new status: ')
         print('task edited successfully')          
    else:
        print('Invalid task number')

#view your list
def view_list():
    if len(tasks) == 0:
      print('your To Do List is empty')
    else:
      print('your list: ')  
      for task in tasks:
           print(task)
           print()   
    
#Delete any task you choose
def delete_task():
        if len(tasks) == 0:
            print('no task to delete')
            return
        elif len(tasks) > 0:
            view_list()
            task_num=int(input('enter the task number to delete :'))
        if task_num <= len(tasks):
            tasks.pop(task_num-1)
            print('the task deleted Successfully')
        else:
            print('invalid task number')

#Edit task status                           
def edit_status():
     if len(tasks) == 0:
          print('There is no tasks to edit its status')
          return
     view_list()
     task_num = int(input('Enter the number of task you want to edit its status: '))
     if task_num <= len(tasks):
              task = tasks[task_num-1]
              print('\nUpdate status for the task: ')
              print(task)
              task.status = input('Enter the new status: ')
              
     else:
              print('Invalid task number')  

def ascending_order():
     if len(tasks) == 0:
          print('your list is empty')
          return
     tasks.sort(key=lambda x: x.name)
     view_list()

def descending_order():
     if len(tasks) == 0:
          print('your list is empty')
          return
     tasks.sort(reverse=True, key=lambda x: x.name)
     view_list() 

def move_task():
     if len(tasks) == 0:
          print('to do list is empty')
          return
     len(tasks) > 0          
def main():
    while True:
        show_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            add_task()
        elif choice == '2':
            edit_task()
        elif choice == '3':
            view_list()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            edit_status()
        elif choice == '6':
             ascending_order()
        elif choice == '7':
             descending_order()        
        elif choice == '8':
            print('Good Bey!')         
            break
        else:
            print('Invalid choice , choose number between 1 and 6')
        
             
if __name__ == '__main__':
            main()