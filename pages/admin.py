from django.contrib import admin
from .models import Boards, Board_menu, SummerNote, File
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget

from django import forms
# Register your models here.

class BasicModelAdmin(SummernoteModelAdmin):
    b_title = forms.CharField(widget=SummernoteWidget())

admin.site.register(Boards, BasicModelAdmin)
admin.site.register(Board_menu)
admin.site.register(File,BasicModelAdmin )