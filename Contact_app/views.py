from django.shortcuts import render
from django.contrib import messages
from Contact_app.models import *
from Home_app.models import *
def contact(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    if request.method == 'POST':
        name =request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        message =request.POST['message']
        #sentTime =request.POST['sentTime']
        if len(name)<6 or len(phone)<11 or len(email)<6 or len(message)<10:
            messages.error(request, "Fail! Please, fill up the form correctly,You missed something")
        else:
            messages.success(request, " thank you ! Your message has been sent successfully. we will contact with you soon ")
        contact = Contact( name=name, email=email, message=message, phone=phone)
        contact.save()
    return render(request, 'contact_app/contact.html', context={'about_inform': about_inform})
