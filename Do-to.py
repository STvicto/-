task = set()
task_F = set()
task_T = set()
while True:
    WDYW = input("Что вы хотите? просмотреть все задачи,посмотреть статус всех задач добавить задачу,\n убрать задачу, посмотреть выполненые задачи, посмотреть незаконченные задачи\n изменить статус задачи, посмотреть статус задачи\n \n")
    if WDYW == "посмотреть все задачи":
        print(task)
    elif WDYW == "добавить задачу":
        taskadd = (input("Введите задачу"))
        if taskadd in task:
           print("такая задачу уже есть")
        else:
         task.add(taskadd)
         task_F.add(taskadd)
         if input("Вы хотите добавить еще задачу?") == "да":
             taskAdd = input("введите задачу которую хотите добавить")
             if taskAdd in task:
              print("такая задачу уже есть")
             else:
                task.add(taskAdd)
                task_F.add(taskAdd)
           
    elif WDYW == "убрать задачу":
        try:
            taskremove = (input("какую задачу вы хотите убрать"))
            task.remove(taskremove)
            if taskremove in task_F:
               task_F.remove(taskremove)
            else:
               task_T.remove(taskremove)
        except Exception as e:
            print("такой задачи нету")
        if input("вы хотите убрать другую задачу?") == "да":
         try:
            task.remove(input("какую задачу вы хотите убрать"))
         except Exception as e:
            print("такой задачи нету")

    elif WDYW == "посмотреть выполненные задачи":
        if task_T == {}:
         print("у вас нет выполненых задач")
        else:
         print(task_T)
    elif WDYW == "посмотреть невыполненные задачи":
         if len(task_F) == 0:
          print("у вас нет законченных задач")
         else:
          print(task_F)
    elif WDYW == "изменить статус задачи":
       TaskRemove = input("статус какой задачи вы хотите изменить? ")
       if TaskRemove in task_T:
          task_T.remove(TaskRemove)
          task_F.add(TaskRemove)
          print("статус удачно сменен")
       else:
          task_F.remove(TaskRemove)
          task_T.add(TaskRemove)
          print("статус удачно сменен")
    elif WDYW == "посмотреть статус задачи":
       Tasklook = input("Введите задачу статус который вы хотите посмотреть")
       if Tasklook in task_T:
          print("эта задача выполнена!")
       if Tasklook in task_F:
          print("Эта задача не выполнена")
       if Tasklook not in task_T and Tasklook not in task_F and Tasklook not in task:
          print("Вашей задачи нету")
       if Tasklook not in task_T and Tasklook not in task_F and Tasklook  in task:
          print("ваша задача нейтральна")
    elif WDYW == "посмотреть статус всех задач":
       for i in task_F:
          print("не выполненые: {}".format(i))
       for i in task_T:
          print("Выполненые: {}".format(i))