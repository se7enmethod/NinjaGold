from django.shortcuts import render, redirect
from time import gmtime, strftime
import random


def index(request):
    # where we make the stuffs
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if 'messages' not in request.session:
        request.session['messages'] = []
    # also redirects from process to here
    # context time and messages
    context = {
        "time": strftime("%m-%d-%Y %H:%M %p", gmtime()), "messages": request.session['messages']
    }
    return render(request, "main.html", context)


def process(request):
    time = strftime("%m-%d-%Y %H:%M %p", gmtime())
    if request.method == "POST":
        print(request.POST)
        if 'farm' in request.POST:
            print("from the farm")
            gold = random.randint(10, 20)
            message = "Earned " + str(gold) + " from the farm! " + time
        elif 'cave' in request.POST:
            print("from the cave")
            gold = random.randint(5, 10)
            message = "Earned " + str(gold) + " from the cave! " + time
        elif 'house' in request.POST:
            print("from the house")
            gold = random.randint(2, 5)
            message = "Earned " + str(gold) + " from the house! " + time
        elif 'casino' in request.POST:
            print("from the casino")
            gold = random.randint(-50, 50)
            if gold > 0:
                message = "Earned " + str(gold) + \
                    " gold from the casino! " + time
            else:
                message = "Lost " + str(gold) + \
                    " gold from the casino... " + time
        request.session['counter'] += gold
        request.session['messages'].append(message)
        request.session.save()
    return redirect("/")


def reset(request):
    # voosh
    request.session.flush()
    return
