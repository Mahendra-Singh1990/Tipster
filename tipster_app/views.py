from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# This view is the home page of website

def index(request):
	return render(request,'tipster_app/index.html')

def contact(request):
	return render(request,'tipster_app/contact.html')

def about(request):
	return render(request,'tipster_app/about.html')

def services(request):
	return render(request,'tipster_app/services.html')

def contactus(request):
    if request.method == 'POST':


        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        final_message = f'Name: {name}\nEmail Address: {email}\nPhone Number: {phone}\nCustomer Query: {message}'
        #print(message)
        send_mail('Customer Query',final_message,settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER,],fail_silently = False)
        #return render(request,'todo/email.html',{'email':email}
        messages.info(request, 'We have received your message. Our team will get in touch with you shortly.')
        #return redirect('home')
        return render(request,'tipster_app/contact.html')
    else:
        return render(request,'tipster_app/contact.html')
