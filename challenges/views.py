from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
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
    "december": "Learn Django for at least 20 minutes every day!"
}  # dictionary: key-value paires

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month in range(1, 13):  # month >= 1 & month < 13!
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month]) # e.g. /challenges/january 
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("<h1>This input is not supported!</h1>")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
    except:
        return HttpResponseNotFound("<h1>This input is not supported!</h1>")
    return HttpResponse(response_data)

def month_selection(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    # response_data = """
    #     <ul>
    #         <li><a href="/challenges/1">January</a></li>
    #         <li><a href="/challenges/2">Feburary</a></li>
    #         <li><a href="/challenges/3">March</a></li>
    #         <li><a href="/challenges/4">April</a></li>
    #         <li><a href="/challenges/5">May</a></li>
    #         <li><a href="/challenges/6">June</a></li>
    #         <li><a href="/challenges/7">July</a></li>
    #         <li><a href="/challenges/8">August</a></li>
    #         <li><a href="/challenges/9">September</a></li>
    #         <li><a href="/challenges/10">October</a></li>
    #         <li><a href="/challenges/11">November</a></li>
    #         <li><a href="/challenges/12">December</a></li>
    #     </ul>
    # """

    return HttpResponse(response_data)
