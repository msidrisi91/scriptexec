from django.shortcuts import render
from subprocess import run, PIPE
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# view before button is any clicked
def initial_view(request):
    return render(request,'home.html',{})


def executeScript_view(request, *args, **kwargs):
    # Script to be executed present in the root directory
    # Can be replaced by another file path using // example: "templates//file.py"
    filename = "script.py"

    # Executes the file and store output, error code and execution related info in byte string format
    output = run([sys.executable, os.path.join(BASE_DIR, filename), ''], shell=False, stdout=PIPE)

    # Extract output and convert to string from byte string
    output = ( output.stdout ).decode('utf-8')

    return render(request, 'home.html', {'output': output})


def platform_view(request, *args, **kwargs):
    flag=1
    return render(request, 'home.html', {'flag':flag})

