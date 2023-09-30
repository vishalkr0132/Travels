
from urllib import request
from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from adminsite.models import Image_Upload, Package_Upload, PopularDestination, UserDetail, DestinationBooking
# Create your views here.
from tokenize import group
from django.contrib.auth.models import Group, User

def index(request):
    Bannner_detail = Image_Upload.objects.order_by('-created_at')
    Package_detail = Package_Upload.objects.order_by('-created_at')[:4]
    Destination = PopularDestination.objects.order_by('-created_at')
    products = {"Bannner_detail":Bannner_detail, "Package_detail":Package_detail, "Destination":Destination }
    return render(request,'index.html', products)

def about(request):
    return render(request,'about.html')

def services(request):
    destination = PopularDestination.objects.all()
    products = {"destination":destination}
    return render (request,'services.html', products)

def packages(request):
    Package_detail = Package_Upload.objects.order_by('-created_at')
    popular_place = PopularDestination.objects.order_by('-created_at')
    
    product = {"Package_detail":Package_detail, "popular_place":popular_place}
    return render (request,'packages.html', product)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        messege = request.POST.get("message")

        contact_details = Contact(name=name, email=email, mobile=phone, message=messege)
        contact_details.save()
        return redirect("/")
    else:
        return render (request,'contact.html')

def booking(request):
    return render (request,'booking.html')

def about_place(request, pid):
    pid = int((pid))
    # print(pid)
    place_detail = PopularDestination.objects.filter(id = pid)
    product = {'place_detail':place_detail}
    return render(request, 'place_deteil.html', product)

def register_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        user_data = UserDetail(name=name, email=email, username=email, phone=phone, password=password)
        user_data.save()
        user = User.objects.create_user(email, email, password)
        my_group = Group.objects.get(name="normal_user")
        my_group.save()
        user.save()
        return redirect("/")
    else:
        return render (request, 'create_user.html')

def bookingdestination(request, pid):
    if request.method =="POST":
        username = request.user.username
        destination_id = request.POST.get('destination_id')
        destination_pack = request.POST.get('destination_pack')
        destination_location = request.POST.get('destination_location')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        no_of_days = request.POST.get('no_of_days')
        no_of_person = request.POST.get('no_of_person')
        data = DestinationBooking(usename=username, destination_id=destination_id, 
                                  destination_pack=destination_pack,
                                  destination_location=destination_location,
                                  name = name, phone = phone, email=email,
                                  starting_date = start_date, ending_date = end_date,
                                  no_of_days=no_of_days, no_of_person=no_of_person, destinatoin_prise= 0, total_prise=0)
        data.save()
    pid = int(pid)
    username = request.user.username
    user_data = UserDetail.objects.filter(username=username)
    place_detail = PopularDestination.objects.filter(id = pid)
    product = {'place_detail':place_detail, 'user_data':user_data}
    return render (request, 'bookingdestination.html', product)

def user_profile(request):
    return render(request, 'user_profile.html')