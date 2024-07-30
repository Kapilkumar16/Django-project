from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):

    peoples=[
        {'name' : 'Abhinash' , 'age':26},
        {'name' : 'Kapil' , 'age':17},
        {'name' : 'Shivam' , 'age':25},
        {'name' : 'PP' , 'age':26},
    ]


    vegetables = ['Pumpkin' , 'Tomato' , 'Potatoe']

    return render(request, "home/index.html", context={'peoples': peoples,'vegetables':vegetables , 'page' :'Django'})

def about(request):
    context= {'page': 'About'}
    return render(request, "home/about.html" , context)

def contact(request):
    context= {'page': 'Contact'}
    return render(request, "home/contact.html" ,context)