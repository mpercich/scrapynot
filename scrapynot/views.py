from django.shortcuts import render
import datetime

def hello(request):
    now = datetime.datetime.now()
    return render(request, 'current_date.html', {'current_user': request.user, 'current_date': now})