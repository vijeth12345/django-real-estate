from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has registered
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have alreay contacted with this listing')

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # Send Email
        # send_mail(
        #     'Property Listing Enqiry',
        #     'There has been an enquiry for '+listing,
        #     'vijeth@realmimpex.com',
        #     [realtor_email, 'vijethsimha71@gmail.com'],
        #     fail_silently=False

        # )
        messages.success(
            request, 'Thanks for contacting us wil get in touch with you shortly')
        return redirect('/listings/'+listing_id)

    # return redirect('listing')
