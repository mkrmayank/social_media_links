from datetime import date
from django.shortcuts import redirect, render, HttpResponse
# from datetime import date, datetime
from social.models import Register

# Create your views here.
def index(request):
    details = Register.objects.all()
    context = {'details':details}
    return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage")


def register(request):
    if request.method == "POST":

        name = request.POST.get('name')
        number = request.POST.get('number')
        designation = request.POST.get('designation')
        about = request.POST.get('about')
        social1 = request.POST.get('social1')
        social2 = request.POST.get('social2')
        social3 = request.POST.get('social3')
        social4 = request.POST.get('social4')
        social5 = request.POST.get('social5')

        img = request.FILES['img'] if len(request.FILES) != 0 else request.FILES
        register = Register(img=img, name=name, number=number, designation=designation, about=about, social1=social1, social2=social2, social3=social3, social4=social4,social5=social5)
        register.save()
    return render(request, 'register.html')
    
