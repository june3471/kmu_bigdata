from django_summernote import fields as summer_fields
from .models import SummerNote, File
from django import forms

class PostForm(forms.ModelForm):
     fields = summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
     class Meta:
           model = SummerNote
           fields = ('fields', )




class UploadFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('f_title', 'f_file')

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['f_file'].required = False