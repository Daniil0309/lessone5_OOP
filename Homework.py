#Менеджер задач
#Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи,
#срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и
#вывода списка текущих (не выполненных) задач.
class task:
    def __init__(self, Task_description, Task_period, Task_status):
        self.Task_description = Task_description #описание задачи
        self.Task_period = Task_period #срок выполнения
        self.Task_status = Task_status #статус

    def add_task(self):
        print(f"Задача {self.Task_description} добавлена")

    def done_task(self):
        if self.Task_status == True:
            print(f"Задача {self.Task_description} выполнена")
        else:
            print(f"Задача {self.Task_description} не выполнена")


    def list_task(self):
        if self.Task_status == False:
            print(f"Список задач: {self.Task_description}")

    def info(self):
        print(f"Описание задачи - {self.Task_description}")
        print(f"Срок выполнения - {self.Task_period}")
        print(f"Статус - {self.Task_status}")


task1 = task("Выпить воды", "13:00", False)
task2 = task("Покушать", "14:00", True)
task3 = task("Погулять", "15:00", False)
task4 = task("Помыть посуду", "16:00", True)

task1.add_task()
task2.add_task()
task3.add_task()
task4.add_task()

task1.done_task()
task2.done_task()
task3.done_task()
task4.done_task()

task1.info()

