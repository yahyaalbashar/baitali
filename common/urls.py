from django.urls import path
from .views import home
from common.api.views import (
    #List views
    ListFAQAPIView, 
    ListHeroSliderItemAPIView,
    ListActivitiesAPIView,
    ListRoomsAPIView,
    ListFacilityAPIView,
    ListGalleryImages,

    #Retrieve views
    RetrieveActivityAPIView,
    RetrieveRoomAPIView,

    #Create Views
    CreateContactUsAPIView
    )

urlpatterns = [
    path('', home, name='home'),
    path('api/list-faqs', ListFAQAPIView.as_view(), name="faq_list_api"),
    path('api/list-slider-images', ListHeroSliderItemAPIView.as_view(), name="slider_images_list_api"),
    path('api/list-activities', ListActivitiesAPIView.as_view(), name="activity_list_api"),
    path('api/get-activity/<int:pk>', RetrieveActivityAPIView.as_view(), name="activity_get_api"),
    path('api/contact-us', CreateContactUsAPIView.as_view(), name="create_contact_us_api"),
    path('api/list-rooms', ListRoomsAPIView.as_view(), name="list_rooms"),
    path('api/get-room', RetrieveRoomAPIView.as_view(), name="get_room"),
    path('api/list-facilities', ListFacilityAPIView.as_view(), name="list_facilities"),
    path('api/list-gallery-images', ListGalleryImages.as_view(), name="list_gallery_images"),


]