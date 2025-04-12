from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
import pytz

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


