daily_task_dict={'clean room':{'priority level':'medium','done':True},
                 'clean home': {'priority level':'high  ', 'done': False},
                 'breakfast ':{'priority level':'high  ','done':True},
                 'laundry   ':{'priority level':'low   ','done':False},
                 'sport     ':{'priority level':'medium','done':True}}



def menu():
    user_choice=input('Please enter your choice: \n1.for all information \n2.to status \n3.to Urgent tasks \n4.to sum up \n0.to exit')
    if user_choice=='1':
        print_all_tasks(daily_task_dict)
    elif user_choice=='2':
        print(f'task completed: {status_completed(daily_task_dict)[0]} incomplete: {status_completed(daily_task_dict)[1]}')
    elif user_choice=='3':
        print(f'\nthere are {urgently_tasks(daily_task_dict)} urgently tasks\n')
    elif user_choice=='4':
        pass
    elif user_choice=='0':
        print('Goodbye')
        exit()







def print_all_tasks(task_dict):
    print('  name       |   priority level   |    done')
    print('_____________|____________________|____________')
    for key,value in task_dict.items():
        task=key

        print(f'{task}   |   {value["priority level"]}           |     {'completed' if value["done"] else 'incomplete'}')
        print('_____________|____________________|_____________')





def status_completed(task_dict):
    completed=0
    incompleted=0
    for key,value in task_dict.items():
        if value["done"]:
            completed+=1
        else:
            incompleted+=1

    return completed, incompleted


def urgently_tasks(task_dict):
    urgently=0
    for key,value in task_dict.items():
        if value["priority level"]=='high  ':
            urgently+=1
    return urgently



def sum_up(task_dict):
    sum=0
    for key in task_dict.keys():
        sum+=1
    print(sum)


# menu()





def tasks_management():
    while True:
        menu()

tasks_management()