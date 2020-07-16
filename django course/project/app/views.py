from django.shortcuts import render
from app.models import ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def contact_form(request):
    return render(request,'app/contact_form.html')

def portfolio(request):
    return render(request,'app/portfolio.html')


def about(request):
    """This view render about.html page
    parameters: HttpRequest
    return: nothing  """
    return render(request,'app/about.html')


def contact(request):
    """This view render contact.html page
    parameters: HttpRequest
    return: nothing  """
    return render(request,'app/contact.html')

#Contact Form Data Submit form view
def contact_form_submit(request):
    """This view take post method and submit form details 
        by creating ContactForm Model object
    parameters: HttpRequest
    return: if form data submit successfully then 
            HttpResponseRedirect to page contact.html  """
    if request.method == "POST":
        full_name = request.POST['full_name']
        email_id = request.POST['email_id']
        contact_number = request.POST['contact_number']
        message = request.POST['message']
        ContactForm.objects.create(full_name=full_name,
                                   email_id=email_id,
                                   contact_number=contact_number,
                                   message=message
                                   )
    return HttpResponseRedirect(reverse('app:contact'))

#All Data View
def all_data(request):
    """This view render all_data.html page
    parameters: HttpRequest
    return: contact_data  """
    contact_data = ContactForm.objects.all()
    data = {'contact_data':contact_data}
    return render(request,'my_portfolio_website_app/all_data.html',data)
