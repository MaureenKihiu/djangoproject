from django.shortcuts import render

import datetime

# Create your views here.


def kihiu(request):
    now = datetime.datetime.now()
    return render(request, "index2.html", {
        "new": now.month == 4 and now.day == 4

    })


