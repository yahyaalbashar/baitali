from datetime import datetime
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    CreateAPIView
    )

from common.models import (
    FAQ, 
    HeroSliderItem, 
    Activity,
    ContactUs
    )
from common.api.serializers import (
    FAQSerializer, 
    HeroSliderItemSerializer, 
    ActivitySerializer,
    ContactUsSerializer
    )


class ListFAQAPIView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class ListHeroSliderItemAPIView(ListAPIView):
    queryset = HeroSliderItem.objects.all()
    serializer_class = HeroSliderItemSerializer


class ListActivitiesAPIView(ListAPIView):
    queryset = Activity.objects.all().filter(date__gte=datetime.now())
    serializer_class = ActivitySerializer


class RetrieveActivityAPIView(RetrieveAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class CreateContactUsAPIView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer