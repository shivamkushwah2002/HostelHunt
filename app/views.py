from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.decorators import login_required
from app.models import Listing
from app.models import Listing
from .forms import ListingForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User,Group
from .decorators import *
from django.contrib import messages
from .forms import ListingForm  
from .models import Listing
from app.models import Listing  


def index(request):
    
    return render(request,'index.html')


def home(request):
    search_location = request.GET.get('search_location', '').strip()
    if search_location:
        listings = Listing.objects.filter(location__icontains=search_location)
        if not listings.exists():
            listings = Listing.objects.filter(college__icontains = search_location)
            if not listings.exists:
                no_results=True

            else:
                no_results = False
        else:
            no_results = False
    else:
        listings = Listing.objects.all()
        no_results = False
    
    context = {
        'listings': listings,
        'no_results': no_results,
        'search_location': search_location,
    }
    return render(request, 'home.html', context)

@role_required('owner')
def listing(request):
    if request.method == 'POST':

        room = request.POST.get('room')
        hostel_name=request.POST.get('hostel')
        roomtype = request.POST.get('roomtype')
        owner_name = request.POST.get('Owner_Name')
        loc = request.POST.get('location')
        rent = request.POST.get('rent')
        beds=request.POST.get('beds')
        contact = request.POST.get('contact')
        college = request.POST.get('college')
        landmark = request.POST.get('landmark')
        wifi = request.POST.get('wifi')
        meals=request.POST.get('meals')
        homeservice = request.POST.get('homeservice')
        typeroom=request.POST.get('typeroom')
        laundry=request.POST.get('laundry')
        description = request.POST.get('description')
        img = request.FILES.get('image')  

        new_listing = Listing(
            hostel_name=hostel_name,
            room=room,
            college=college,
            landmark=landmark,
            beds=beds,
            wifi=wifi,
            home_service=homeservice,
            meals=meals,
            type_room=typeroom,
            laundry=laundry,
            owner=owner_name,
            room_type=roomtype,
            location=loc,
            rent=rent,
            contact_info=contact,
            description=description,
            image=img 
        )
        new_listing.save()
        return redirect('home')  
    else:
        form = ListingForm()

    return render(request, 'listing.html', {'form': form})

@login_required(login_url='/login')
def view_details(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request, 'view_details.html', {'listing': listing})

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home') 
        else:
            return render(request,'login.html')
        
    return render(request,'login.html')

def register(request):
    GROUP_MAPPING = {
        'owner': 'owner',
        'user': 'user'
    }
    
    if request.method == 'POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user_type = request.POST.get('user_type')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'register.html')
        
        if user_type not in GROUP_MAPPING:
            messages.error(request, 'Invalid user type selected')
            return render(request, 'register.html')
        
        try: 
            
                user = User.objects.create_user(
                    username=username,
                    first_name = firstname,
                    last_name = lastname,
                    email=email,
                    password=password1
                )
                
                group_name = GROUP_MAPPING[user_type]
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
                
                return redirect('login')
                
        except Group.DoesNotExist:
            return render(request, 'register.html')
        except Exception as e:
            return render(request, 'register.html')
    
    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('index')

@role_required('owner')
def owner(request):
    return render(request, 'owner.html')



@login_required
def profile(request):
    user_listings = Listing.objects.filter(owner=request.user)
    context = {
        'user_listings': user_listings
    }
    return render(request, 'profile.html', context)


@login_required
def delete_listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id, owner=request.user)
    listing.delete()
    return redirect('profile') 


def update_listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id, owner=request.user)
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('/profile')  
    else:
        form = ListingForm(instance=listing)
    return render(request, 'update_listing.html', {'form': form})