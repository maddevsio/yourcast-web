from django.contrib import admin
from .models import Stream, Category, CategoryBackground
from .forms import StreamForm

class StreamAdmin(admin.ModelAdmin):
    form = StreamForm

admin.site.register(Category)
admin.site.register(CategoryBackground)
admin.site.register(Stream, StreamAdmin)
