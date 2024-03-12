from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib import messages
def partnership_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        send_mail(
            subject,
            f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}",
            'ethiozele4443@gmail.com',  # Sender's email address
            ['ethiozele4443@gmail.com'],  # List of recipient email addresses
            fail_silently=False,
        )
        messages.success(request, 'Your message has been sent successfully!')
        # Redirect after submission (optional)
        return HttpResponseRedirect(reverse('partnership_form'))  # Redirect to the same page
    else:
        return render(request, 'partnership.html')
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        send_mail(
            subject,
            f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}",
            'ethiozele4443@gmail.com',  # Sender's email address
            ['ethiozele4443@gmail.com'],  # List of recipient email addresses
            fail_silently=False,
        )
        messages.success(request, 'Your message has been sent successfully!')
        # Redirect after submission (optional)
        return HttpResponseRedirect(reverse('contact_form'))  # Redirect to the same page
    else:
        return render(request, 'contact.html')
def index_web(request):
    return render(request, 'index_web.html')  
def about(request):
    return render(request, 'about.html')
def gallery(request):
    return render(request, 'gallery.html')
def partnership(request):
    return render(request, 'partnership.html')
def projects(request):
    return render(request, 'projects.html')
def blog(request):
    return render(request, 'blog.html')   
def contact(request):
    return render(request, 'contact.html')