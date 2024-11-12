from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monworks = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None,
}

def monworkstr(request, month):
    try:
        work_for_month = monworks[month]
        return render(request, "challenges/challenge.html", {
            "challenge": work_for_month,
            "month_name": month,
        })
        
    except:
        return HttpResponseNotFound("Month not found!")
    

def monworkint(request, month):
    months = list(monworks.keys())
    if month <= len(months):
        redirect_month = months[month-1]
        redirect_path = reverse("int_month", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("Invalid Month")
    
# def months(request):
#     month_response = ""
#     for month in monworks.keys():
#         page = reverse("int_month", args=[month])
#         month_response += f"<li><b><a href=\"{page}\">{month}</a></b></li>"
#     final_response = f"<url>{month_response}</url>"
#     return HttpResponse(final_response)



def months(request):
    month = list(monworks.keys())
    return render(request, "challenges/index.html", {
        "month" : month
    })
    