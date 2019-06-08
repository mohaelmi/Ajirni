from django.shortcuts import render
from rest_framework import generics
from .serializers import ItemsSerializer, LikesSerializer
from .models import Items, Likes
from django.http import HttpResponse

# Create your views here.


class CreateItem(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Item."""
        serializer.save()


class Search(generics.ListAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self):
        """
        Optionally serach fields,
        by filtering against query parameters in the URL.
        """
        queryset = Items.objects.all()
        status = self.request.query_params.get('status', 'Avilable')
        confirmed = self.request.query_params.get('confirmed', 'True')
        name = self.request.query_params.get('name', '')
        description = self.request.query_params.get('description', '')
        condition = self.request.query_params.get('condition', '')
        category_id = self.request.query_params.get('category_id', '')
        no_rooms = self.request.query_params.get('no_rooms', '')
        no_bathrooms = self.request.query_params.get('no_bathrooms', '')
        surface_area = self.request.query_params.get('surface_area', '')
        furnished = self.request.query_params.get('furnished', '')
        location = self.request.query_params.get('location', '')
        price = self.request.query_params.get('price', '')
        floor_no = self.request.query_params.get('floor_no', '')
        car_make = self.request.query_params.get('car_make', '')
        year_manufactured = self.request.query_params.get(
            'year_manufactured', '')
        no_killometers = self.request.query_params.get('no_killometers', '')
        fuel = self.request.query_params.get('fuel', '')
        color = self.request.query_params.get('color', '')
        transmission = self.request.query_params.get('transmission', '')

        queryset = queryset.filter(
            status__icontains=status,
            confirmed__icontains=confirmed,
            name__icontains=name,
            description__icontains=description,
            condition__icontains=condition,
            category_id__icontains=category_id,
            no_rooms__icontains=no_rooms,
            no_bathrooms__icontains=no_bathrooms,
            surface_area__icontains=surface_area,
            furnished__icontains=furnished,
            location__icontains=location,
            price__icontains=price,
            floor_no__icontains=floor_no,
            car_make__icontains=car_make,
            year_manufactured__icontains=year_manufactured,
            no_killometers__icontains=no_killometers,
            fuel__icontains=fuel,
            color__icontains=color,
            transmission__icontains=transmission
        )
        return queryset


class LikeItem(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

    def perform_create(self, serializer):
        """add like for item"""
        serializer.save()

    def get_queryset(self):
        queryset = Likes.objects.all()
        item_id = self.request.query_params.get('item_id', None)
        queryset = queryset.filter(item_id__exact=item_id)
        return queryset
