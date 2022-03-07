from django.shortcuts import render

# Create your views here.
def indice(request):
  return render(request,"index.html")

import git
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update(request):
  if request.method == "POST":
    print(request.POST)
    if request.POST.ref!="refs/heads/main":
      return HttpResponse("Invalid branch. Update aborted")
    '''
    pass the path of the directory where your project will be 
    stored on PythonAnywhere in the git.Repo() as parameter.
    Here the name of my directory is "test.pythonanywhere.com"
    '''
    repo = git.Repo("realod/") 
    origin = repo.remotes.origin

    origin.pull()

    return HttpResponse("Updated code on PythonAnywhere!")
  else:
    return HttpResponse("Couldn't update the code on PythonAnywhere")