from django.shortcuts import render
from time import localtime, strftime
def index(request):
    datetime = strftime("%b-%d-%Y %I:%M%p", localtime()).split()
    context = {
        "fecha": datetime[0],
        "hora": f"{datetime[1]}",
    }
    return render(request, "index.html", context)

