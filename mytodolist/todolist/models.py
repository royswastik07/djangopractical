from django.db import models
import datetime
import uuid      #uuid having 18 char hexadecimal code 

# Create your models here.
class ToDoList(models.Model):
    taskid = models.UUIDField(auto_created=True , primary_key=True,default= uuid.uuid4)
    task_title = models.TextField(max_length=255,blank=False)
    task_description = models.TextField(null=True)
    task_created_on = models.DateTimeField(default=datetime.datetime.now())
    task_completed_on = models.DateTimeField(blank=True,null=True)

    # def __str__(self):
    #     return self.task_title[:50]
