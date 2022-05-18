
from django.shortcuts import redirect, render



from .models import Urun,Alici
from django.contrib.auth.models import User
from .forms import FormUrun
# Create your views here.

def index(request):

   if request.method == 'POST':
      form = FormUrun(request.POST,request.FILES)
      if form.is_valid():
         form.save()
         return redirect('home')
      return redirect('home')
   else :
      form = FormUrun()
   context = {
      'uruns':Urun.objects.all(),
      'alici':Alici.objects.all(),
      'form':form

   }
   
   return render(request,'index.html',context)

def filter(request,id):
   user = Urun.objects.get(id=id).author
   print(user)
   data = Urun.objects.filter(author=user)
   return render(request,'filter.html',{'uruns':data})
