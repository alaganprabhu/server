from django.shortcuts import render,redirect
from .models import Visit

def main(request):
    data=Visit.objects.all()
    if(data!=""):
        return render(request,"index.html",{"datas":data})
    else:
        return render(request,"index.html",{})
    
def addData(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        message=request.POST['message']

        obj=Visit()
        obj.Name=name
        obj.Email=email
        obj.Mobile=mobile
        obj.Message=message
        obj.save()
        data=Visit.objects.all()
        # messages.success(request,'Your Message Sent!')
        # return redirect(request,"index.html",{"datas":data})
        return redirect(main)
    return render(request,'index.html')
