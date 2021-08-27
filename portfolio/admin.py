from django.contrib import admin
from .models import Testimonial, Vaardigheid_web, Vaardigheid_data, Vaardigheid_overig, Intro


admin.site.register(Testimonial)
admin.site.register(Vaardigheid_web)
admin.site.register(Vaardigheid_data)
admin.site.register(Vaardigheid_overig)
admin.site.register(Intro)
