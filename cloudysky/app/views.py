
from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
import pytz
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

def index(request):
    # 1) build a simple bio list
    bio = [
        {'name': 'Charlie', 'role': 'Frontend'},
        {'name': 'Charlie',   'role': 'Backend'},
        {'name': 'Charlie', 'role': 'Design'},
    ]
    # 2) current time as string
    now = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'app/index.html', {
        'bio': bio,
        'current_user': request.user,
        'now': now,
    })

def new_user_form(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    return render(request, 'app/new_user.html')
@csrf_exempt
def create_user(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("POST required")
    username = request.POST.get('user_name')
    email    = request.POST.get('email')
    password = request.POST.get('password')
    is_admin = request.POST.get('is_admin') == '1'    # check duplicate
    if User.objects.filter(email=email).exists():
        return JsonResponse({'error': 'Email already taken'}, status=400)
    # create & sign in
    user = User.objects.create_user(username=username, email=email, password=password)
    user.is_staff = is_admin
    user.save()
    login(request, user)
    return JsonResponse({'message': 'User created successfully'})

def dummypage(request):
    return HttpResponse("No content here, sorry!")
def get_time(request):
    # Set Central Time using the America/Chicago timezone
    central_tz = pytz.timezone("America/Chicago")
    # Get the current UTC time, then convert to Central Time
    now_central = datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(central_tz)
    # Format the time as HH:MM (for example, "13:24")
    time_str = now_central.strftime("%H:%M")
    return HttpResponse(time_str)

def get_sum(request):
    # Get query parameters n1 and n2, defaulting to '0' if not provided
    try:
        n1 = float(request.GET.get('n1', '0'))
        n2 = float(request.GET.get('n2', '0'))
        result = n1 + n2
    except (TypeError, ValueError):
        # Return 400 status code for invalid input
        return HttpResponse("Invalid input", status=400)
    # Return the sum as a string
    return HttpResponse(str(result))


