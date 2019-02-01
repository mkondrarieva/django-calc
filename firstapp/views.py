from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def evklid(a,b):
    if a<0:
        a=-a
    if b<0:
        b=-b
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a
def add(num1,denum1,num2,denum2):
    num=int(num1)*int(denum2)+int(denum1)*int(num2)
    denum=int(denum1)*int(denum2)
    if num!=0:
        nod=evklid(num,denum)
        num//=nod
        denum//=nod
    if denum<0:
        num=-num
        denum=-denum
    if num<0:
        k=(-num)//denum
        znak='-'
        l=(-num)%denum
    else:
        k=num//denum
        l=num%denum
        znak=''
    q=str(num)+'/'+str(denum)+'='+znak+str(k)+', '+str(l)+'/'+str(denum)+'='+str(num/denum)[0:11]
    return q
def sub(num1,denum1,num2,denum2):
    num=int(num1)*int(denum2)-int(num2)*int(denum1)
    denum=int(denum1)*int(denum2)
    if num!=0:
        nod=evklid(num,denum)
        num//=nod
        denum//=nod
    if denum<0:
        num=-num
        denum=-denum

    if denum<0:
        num=-num
        denum=-denum
    if num<0:
        k=(-num)//denum
        znak='-'
        l=(-num)%denum
    else:
        k=num//denum
        l=num%denum
        znak=''
    q=str(num)+'/'+str(denum)+'='+znak+str(k)+', '+str(l)+'/'+str(denum)+'='+str(num/denum)[0:11]
    return q
def div(num1,denum1,num2,denum2):
    num=int(num1)*int(denum2)
    denum=int(denum1)*int(num2)
    if num!=0:
        nod=evklid(num,denum)
        num//=nod
        denum//=nod
    if denum<0:
        num=-num
        denum=-denum
    if denum<0:
        num=-num
        denum=-denum
    if num<0:
        k=(-num)//denum
        znak='-'
        l=(-num)%denum
    else:
       
        k=num//denum
        l=num%denum
        znak=''
    q=str(num)+'/'+str(denum)+'='+znak+str(k)+', '+str(l)+'/'+str(denum)+'='+str(num/denum)[0:11]
    return q
def mult(num1,denum1,num2,denum2):
    num=int(num1)*int(num2)
    denum=int(denum1)*int(denum2)
    if num!=0:
        nod=evklid(num,denum)
        num//=nod
        denum//=nod
    if denum<0:
        num=-num
        denum=-denum
    if denum<0:
        num=-num
        denum=-denum
    if num<0:
        k=(-num)//denum
        znak='-'
        l=(-num)%denum
    else:
        k=num//denum
        l=num%denum
        znak=''
    q=str(num)+'/'+str(denum)+'='+znak+str(k)+', '+str(l)+'/'+str(denum)+'='+str(num/denum)[0:11]
    return q
def index(request):
    if request.method == "POST":
        num1 = int(request.POST.get("num1"))
        denum1 = int(request.POST.get("denum1"))
        num2 = int(request.POST.get("num2"))
        denum2 = int(request.POST.get("denum2"))
        if 'add' in request.POST:
            name=add(num1,denum1,num2,denum2)
            return HttpResponse("<h2>Result= {0}</h2>".format(name))
        elif 'sub' in request.POST: 
            name=sub(num1,denum1,num2,denum2)
            return HttpResponse("<h2>Result= {0}</h2>".format(name))
        elif 'mult' in request.POST: 
            name=mult(num1,denum1,num2,denum2)
            return HttpResponse("<h2>Result= {0}</h2>".format(name))
        elif 'div' in request.POST: 
            name=div(num1,denum1,num2,denum2)
            return HttpResponse("<h2>Result= {0}</h2>".format(name))
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})




#def index(request):
#    data = {"header": "Hello Django", "message": "Welcome to Python"}
#    return render(request, "index.html", context=data)
