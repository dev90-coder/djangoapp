from django.shortcuts import render
from amrita.models import student,cont,suggests

# Create your views here.
def gallery(requests):
    return render(requests,"gallery.html")

def suggest(requests):
    if requests.method == 'POST':
        names = requests.POST.get('name')
        
        desig = requests.POST.get('desig')
        text = requests.POST.get('s_l')
        sug_f = requests.POST.get('sug_for')
        emails = requests.POST.get('email')
        classes = requests.POST.get('class')
        su = suggests(mem=names,desig=desig,text=text,sug_f=sug_f,emails=emails,classes=classes)
        su.save()
    return render(requests,"suggestion.html")
def abouts(requests):
    return render(requests,"about.html")
def index(requests):
    return render(requests,"index.html")
def corner(requests):

    return render(requests,"corner.html")
def details(requests):
    response=''
    if requests.method == 'POST':
        ad = requests.POST.get('ad')
        phone = requests.POST.get('phone')
        if ad != '':
            
            data = student.objects.filter(addmission=ad,phone=phone)
            print(data)
            try:
                if data[0].student != '':
                    response =''
                
                    return render(requests,"details.html",{"data":data})
                else:
                
                    response='Not found !'
            except:
                response = 'Either phone number or addmission is incorrect'
    return render(requests,"details.html",{"response":response})
def register(requests):
    return render(requests,"registration.html")
def contact(requests):
    if requests.method == 'POST':
        names = requests.POST.get('name')
        mobiles = requests.POST.get('mobile')
        emails = requests.POST.get('email')
        text = requests.POST.get('text')
        dat = cont(name=names,mobile=mobiles,email=emails,comment=text)
        dat.save()
        response = 'Yot message has been sent'
        return render(requests,"contact.html",{"response":response})
    return render(requests,"contact.html")
def admins(requests):
    
    con = cont.objects.all()
    suggestions = suggests.objects.all()
    stu = student.objects.all()

    return render(requests,"admin.html",{"contact":con,"su":suggestions,"student":stu})