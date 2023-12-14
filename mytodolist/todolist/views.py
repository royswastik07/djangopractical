from django.shortcuts import render,redirect,HttpResponse
from .models import ToDoList

# todolist=["Django","Html","Css","JS"]

# Create your views here.
def index(request):
    if request.POST:
        new_task=request.POST["bla"]
        new_desk=request.POST["editor"]
        # todolist.append(new_task.strip())
        #
        todolist = ToDoList(task_title=new_task ,task_description=new_desk)
        todolist.save()
        return redirect("index")
    
    todolist = ToDoList.objects.all()
    # print(todolist)
    return render(request,"todolist/index.html",context={"task":todolist})

def about(request):
    return render(request,"todolist/aboutus.html")

def deleteTask(request,id):
    task=ToDoList.objects.get(taskid=id)
    task.delete()
    return redirect('index')

def editTask(request,id):
    task=ToDoList.objects.get(taskid=id)
    if request.POST:
        new_task=request.POST["bla"].strip()
        new_desk=request.POST["editor"]
        # todolist.append(new_task.strip())
        task.task_title=new_task
        task.task_description=new_desk
        task.save()
        return redirect("index")
    return render(request,"todolist/edittodo.html",context={'task':task})