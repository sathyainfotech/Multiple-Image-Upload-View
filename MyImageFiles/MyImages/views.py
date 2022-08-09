from django.shortcuts import render,redirect
from .forms import MyImageForm
from .models import Image
from django.contrib import messages
import os

# Create your views here.
def home(request):
    mydata=Image.objects.all()
    myform=MyImageForm()
    context={'form':myform,'mydata':mydata}
    return render(request,"index.html",context)

def uploadImage(request):
     if request.method=="POST":    
        myform=MyImageForm(request.POST,request.FILES)               
        if myform.is_valid():              
            for MyFile in request.FILES.getlist('file'):                        
                exists=Image.objects.filter(image=MyFile).exists()
                if exists:
                    data=1
                else:
                    data=0
                    Image.objects.create(image=MyFile).save()  
            if data==1:                
                messages.error(request,'The Image already exists...!!!')
            else:
                messages.success(request,"Image uploaded successfully.")
            return redirect('home')

def deletefile(request,id):
    mydata=Image.objects.get(id=id)    
    mydata.delete()    
    os.remove(mydata.image.path)
    messages.success(request,'File deleted successfully.')  
    return redirect('home')