from django.shortcuts import render
from .models import (
                        FAQ,
                        GalleryImage,
                        SectionText,
                        Activity,
                    )



def home(request):
    faq_list = FAQ.objects.all()
    gallery_images_list = GalleryImage.objects.all()
    sections_list = SectionText.objects.all()
    activities_list = Activity.objects.all()
    context = {
        'faq_list':faq_list,
        'gallery_images_list':gallery_images_list,
        'sections_list':sections_list,
        'activities_list':activities_list


    }
    return render(request, "common/home.html",context)