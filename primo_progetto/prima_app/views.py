from django.shortcuts import render

# Create your views here.
def indice(request):
  return render(request,"index.html")

import git
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import requests


@csrf_exempt
def update(request):
  if request.method == "POST":
    '''
    pass the path of the directory where your project will be 
    stored on PythonAnywhere in the git.Repo() as parameter.
    Here the name of my directory is "test.pythonanywhere.com"
    '''
    
    repo = git.Repo("realod/") 
    origin = repo.remotes.origin
    origin.pull()
    
    username = "Commentatore"
    api_token = "96adb770cf3be1028f4e517c8222d80e5378ef2f"
    domain_name = "Commentatore.pythonanywhere.com"

    response = requests.post(
      'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(
        username=username, domain_name=domain_name
      ),
      headers={'Authorization': 'Token {token}'.format(token=api_token)}
    )
    if response.status_code == 200:
      return HttpResponse("Updated code on PythonAnywhere!")
    else:
      return HttpResponse('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

  else:
    return HttpResponse("Couldn't update the code on PythonAnywhere")