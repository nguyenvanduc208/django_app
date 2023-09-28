from django.db import models
from uuid import uuid4

# Create your models here.

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    git_url = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    status = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "sast_task"
            


class SubTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    status = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "sast_subtask"
    

class Result(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    description = models.CharField(max_length=255)
    severity = models.CharField(max_length=100)
    start_line = models.IntegerField()
    end_line = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "sast_result"