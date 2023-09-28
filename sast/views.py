from django.shortcuts import render
from faker import Faker
from .models import Task, SubTask, Result
import random

BRANCH = ['main', 'develop', 'master', 'feature']
SEVERITY = ['high', 'medium', 'low', 'critical']
STATUS = [True, False]
languages = ['php', 'python', 'js', 'java', 'ruby']

# Create your views here.

def fake_data(resquest):
    print("\n-------------------------------------------------")
    fake = Faker()
    
    # #Tao Task
    # task_ids = []
    # for i in range(300):
    #     git_url = fake.url()
    #     branch = random.choice(BRANCH)
    #     status = random.choice(STATUS)
        
    #     task = Task.objects.create(git_url=git_url, branch=branch, status=status)
        
    #     print("Tao thanh cong: ", str(task.id))
    #     task_ids.append(str(task.id))
    
    # print("\n-------------------------------------------------")
    
    # for i in task_ids:
    #     for lan in languages:    
    #         status = random.choice(STATUS)
    #         subtask = SubTask.objects.create(task_id=i, language=lan, status=status)
    #         print("Tao thanh cong sub: ", str(subtask.id))
        
    # id_list = Task.objects.values_list('id', flat=True)
    # for task_id in id_list:
    #     for sub in SubTask.objects.filter(task_id=task_id):
    #         for i in range(random.randint(30, 100)):
    #             description = fake.name()
    #             severity = random.choice(SEVERITY)
    #             start_line = random.randint(30, 100)
    #             end_line = random.randint(30, 100)
                
    #             result = Result.objects.create(description=description, severity=severity, start_line=start_line, end_line=end_line)
    #             print("Tao result: ",str(result.id))
    
    results = Result.objects.all()

    severity_count = {
        'high': 0,
        'medium': 0,
        'low': 0,
        'critical': 0,
    }
    # Lặp qua các đối tượng và đếm số lần xuất hiện của từng loại severity
    for result in results:
        if result.severity == 'high':
            severity_count['high'] += 1
        elif result.severity == 'medium':
            severity_count['medium'] += 1
        elif result.severity == 'low':
            severity_count['low'] += 1
        elif result.severity == 'critical':
            severity_count['critical'] += 1

    # In kết quả đếm
    print("Số lần xuất hiện của mỗi loại severity:")
    for severity, count in severity_count.items():
        print(f"{severity}: {count}")