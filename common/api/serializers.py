from common.models import (
    FAQ, 
    HeroSliderItem, 
    Activity, 
    ContactUs,
    Room,
    Facility,
    GalleryImage,
    FacilityGalleryImage
    )
from rest_framework import serializers


class FAQSerializer(serializers.ModelSerializer):
    """
    FAQ model serializer
    """
    class Meta:
        model = FAQ
        fields = ["question", "answer"]


class HeroSliderItemSerializer(serializers.ModelSerializer):
    """
    HeroSliderItem model serializer
    """
    class Meta:
        model = HeroSliderItem
        fields = ["name", "image", "description"]


class ActivitySerializer(serializers.ModelSerializer):
    """
    Activity model serializer
    """
    class Meta:
        model = Activity
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):
    """
    ContactUs model serializer
    """
    class Meta:
        model = ContactUs
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    """
    Room model serializer
    """
    class Meta:
        model = Room
        fields = "__all__"


class FacilitySerializer(serializers.ModelSerializer):
    """
    Facility model serializer
    """
    class Meta:
        model = Facility
        fields = "__all__"


class GalleryImageSerializer(serializers.ModelSerializer):
    """
    GalleryImage model serializer
    """
    class Meta:
        model = GalleryImage
        fields = "__all__"


class FacilityGalleryImageSerializer(serializers.ModelSerializer):
    """
    FacilityGalleryImage model serializer
    """
    class Meta:
        model = FacilityGalleryImage
        fields = ["id", "title", "description", "image"]
        depth = 1


class FacilityDetailSerializer(serializers.ModelSerializer):
    facilitygalleryimage_set = FacilityGalleryImageSerializer(many=True)


    class  Meta:
        model = Facility
        fields = ["id", "facilitygalleryimage_set", "title", "image", "description", "icon"]