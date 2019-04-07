from django.shortcuts import render,HttpResponse
from .forms import ProductForm,UpdateForm,DeleteForm
from .models import Product
from django.template import loader
from .models import Reg
from .forms import RegForm,LoginForm

def home(request):
    return render(request,'home.html')

def insert(request):
    if request.method=='POST':
        form=ProductForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            data="<h1>Insertion is sucessful</h1>" \
                 "<a href='/productapp/home'>Goto Home</a>"
            return HttpResponse(data)

        else:
            print(form.errors)

    else:
        form=ProductForm()
        return render(request,'insert.html',{'form':form})

def display(request):
    det=Product.objects.all()
    if len(det)==0:
        data="<h1>No data Found</h1>" \
                 "<a href='/productapp/home'>Goto Home</a>"
        return HttpResponse(data)
    else:
        template=loader.get_template('display.html')
        context={'det':det}
        r=template.render(context,request)
        return HttpResponse(r)

def update(request):
    if request.method=='POST':
        form=UpdateForm(request.POST)
        if form.is_valid():
            id=form.cleaned_data['pid']
            id1=int(id)
            cost=form.cleaned_data['pcost']
            cost1=float(cost)

            dbuser=Product.objects.filter(pid=id1)

            if not dbuser:
                data="<h1>Invalid Product</h1>" \
                "<a href='/productapp/home'>Goto Home</a>"
                return HttpResponse(data)
            else:
                dbuser.update(pcost=cost1)
                data="<h1>Product Upate Sucessful</h1>" \
                 "<a href='/productapp/home'>Goto Home</a>"
                return HttpResponse(data)
        else:
            print(form.errors)

    else:
        form=UpdateForm()
        return render(request,'update.html',{'form':form})

def delete(request):
    if request.method=='POST':
        form=DeleteForm(request.POST)
        if form.is_valid():
            pid1=int(form.cleaned_data['pid'])
            dbuser=Product.objects.get(pid=pid1)

            if not dbuser:
                return HttpResponse('The given Id is not available')

            else:
                dbuser.delete()
                data = "<h1>Product Delete Sucessful</h1>" \
                       "<a href='/productapp/home'>Goto Home</a>"
                return HttpResponse(data)

        else:
            print(form.errors)

    else:
        form = DeleteForm()
        return render(request, 'delete.html', {'form': form})





def home1(request):
    return render(request,'home1.html')

def reg(request):
    if request.method=='POST':
        form=RegForm(request.POST)
        if form.is_valid():
            fname=request.POST.get('fname','')
            lname=request.POST.get('lname','')
            user=request.POST.get('user','')
            pwd=request.POST.get('pwd','')
            mobile=request.POST.get('mobile','')
            email=request.POST.get('email','')
            dob=request.POST.get('dob','')
            gender=request.POST.get('gender','')
            reg=Reg(fname=fname,lname=lname,user=user,pwd=pwd,mobile=mobile,email=email,dob=dob,gender=gender)
            reg.save()
            return HttpResponse('<h1><font color="blue">reg sucess</font></h1>')
    else:
        form=RegForm()
        return render(request,'reg.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=form.cleaned_data['user']
            pwd=form.cleaned_data['pwd']
            dbuser=Reg.objects.filter(user=user)
            dbpwd=Reg.objects.filter(pwd=pwd)

            if not dbuser or dbpwd:
                return render(request,'home.html')
            else:
                 return HttpResponse('<h1>login fail</h1>')

    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})
