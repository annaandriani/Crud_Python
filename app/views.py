from django.shortcuts import render, redirect
from app.forms import AjudaForm
from app.models import Ajuda

def home(request):
    data = {}
    data['db'] = Ajuda.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = AjudaForm()
    return render(request, 'form.html', data)

def create(request):
    form = AjudaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Ajuda.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Ajuda.objects.get(pk=pk)
    data['form'] = AjudaForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Ajuda.objects.get(pk=pk)
    form = AjudaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save
        return redirect('home')

def delete(request, pk):
    db = Ajuda.objects.get(pk=pk)
    db.delete()
    return redirect('home')
