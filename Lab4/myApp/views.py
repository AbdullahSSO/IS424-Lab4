from django.shortcuts import render

# Create your views here.

taxRate = 0.15


def default(request):
    return render(request,"myApp/default.html")


def anyNumber(request,num):
    total = num + (num*taxRate)
    return render(request,"myApp/index.html", {
        "num":num,
        "total":total,
        "taxRate":int(taxRate*100)
    })

def tax(request):
    return render(request,"myApp/tax.html",{
        "taxrate":taxRate*100
    })