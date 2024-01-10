from django.shortcuts import render
from app.forms import * 
from app.models import * 
from django.http import HttpResponse
# Create your views here.
def create_school(request): 

    ESFO=SchoolForm() 
    d={'ESFO':ESFO} 

    if request.method=='POST':
        SFDO=SchoolForm(request.POST) 
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Sname']  
            sp=SFDO.cleaned_data['Sprincipal']  
            sl=SFDO.cleaned_data['Slocation'] 
            e=SFDO.cleaned_data['email']
            re=SFDO.cleaned_data['reenteremail']
            
            SO=School.objects.get_or_create(Sname=sn,Sprincipal=sp,Slocation=sn,email=e,reenteremail=re)[0]
            SO.save() 
            return HttpResponse('school is created') 
        else:
            return HttpResponse('invalid data')

    return render(request,'create_school.html',d)