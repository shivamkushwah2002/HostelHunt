from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'  


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['hostel_name','room','room_type','location','rent','beds','contact_info','college','description','landmark','wifi','home_service','meals','laundry','type_room','image']
        