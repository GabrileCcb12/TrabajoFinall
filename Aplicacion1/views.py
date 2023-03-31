from django.shortcuts import render, redirect
from .forms import MascotaForm
# Create your views here.
def home(request):

    if request.method == 'POST': 
        form =MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmado')
    else:
        form=MascotaForm()
        return render(request,'index.html',{'form': form})
    
def mensaje(request):
    return render (request, 'mensaje.html')


