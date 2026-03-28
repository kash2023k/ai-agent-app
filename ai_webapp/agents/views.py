from django.shortcuts import render
from .crew_logic import run_ai_task

def home(request):
    result = ""

    if request.method == "POST":
        user_input = request.POST.get("task")
        result = run_ai_task(user_input)

    return render(request, "index.html", {"result": result})