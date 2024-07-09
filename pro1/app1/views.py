from django.shortcuts import render, redirect
from .models import Bank
from .forms import BankForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def homeview(request):
    return render(request, 'app1/home.html', {})

@login_required(login_url='/a2/lv/')
def bankview(request):
    form = BankForm()
    if request.method == 'POST':
        form = BankForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/bform.html', {'form':form})

@login_required(login_url='/a2/lv/')
def showview(request):
    obj = Bank.objects.all()
    return render(request, 'app1/show.html', {'obj': obj})

def updateview(request, pk):
    obj = Bank.objects.get(bid=pk)
    form = BankForm(instance=obj)
    if request.method == 'POST':
        form = BankForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/bform.html', {'form':form})

def deleteview(request, x):
    obj = Bank.objects.get(bid=x)
    if request.method == 'POST':
        obj.delete()
        return redirect('/a1/sv/')
    return render(request, 'app1/succees.html', {'obj': obj})