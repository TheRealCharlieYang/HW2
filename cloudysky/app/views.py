from datetime import datetime
import pytz

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import (
    HttpResponse,
    JsonResponse,
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
)
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import login

def index(request):
    # 1) build a simple bio list
    bio = [
        {'name': 'Charlie', 'role': 'Frontend'},
        {'name': 'Charlie', 'role': 'Backend'},
        {'name': 'Charlie', 'role': 'Design'},
    ]

    # 2) current time as string (localized to your server TZ)
    now = timezone.localtime().strftime("%H:%M")

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
    is_admin = request.POST.get('is_admin') == '1'

    # check duplicate email
    if User.objects.filter(email=email).exists():
        return JsonResponse({'error': 'Email already taken'}, status=400)

    # create, flag as admin if requested, save, log in
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    user.is_staff = is_admin
    user.save()
    login(request, user)

    return JsonResponse({'message': 'User created successfully'})

def dummypage(request):
    return HttpResponse("No content here, sorry!")

def get_time(request):
    # Set Central Time using the America/Chicago timezone
    central_tz = pytz.timezone("America/Chicago")
    now_central = datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(central_tz)
    time_str = now_central.strftime("%H:%M")
    return HttpResponse(time_str)

def get_sum(request):
    try:
        n1 = float(request.GET.get('n1', '0'))
        n2 = float(request.GET.get('n2', '0'))
    except ValueError:
        return HttpResponse("Invalid input", status=400)

    return HttpResponse(str(n1 + n2))