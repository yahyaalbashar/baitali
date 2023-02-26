from django.contrib import admin
from .models import (
                        FAQ,
                        GalleryImage,
                        SectionText,
                        Activity,
                        ContactUs,
                        HeroSliderItem
                    
                    )


@admin.register(ContactUs)
class AdminContactUs(admin.ModelAdmin):
    list_display = ['name','mobile', 'subject']


@admin.register(Activity)
class AdminActivity(admin.ModelAdmin):
    list_display = ['title']


@admin.register(SectionText)
class AdminSectionText(admin.ModelAdmin):
    list_display = ['title']


@admin.register(GalleryImage)
class AdminGalleryImage(admin.ModelAdmin):
    list_display = ['title']


@admin.register(FAQ)
class AdminFAQ(admin.ModelAdmin):
    list_display = ['question']


@admin.register(HeroSliderItem)
class AdminHeroSliderItem(admin.ModelAdmin):
    list_display = ['name']