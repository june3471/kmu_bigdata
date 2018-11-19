from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields
from django.utils import timezone

# Create your models here.




class Board_menu(models.Model):
    b_type = models.CharField(max_length=20)
    b_type_ko = models.CharField(max_length=20)
    b_order = models.IntegerField()
    b_descript = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.b_type_ko
class File(models.Model):
    f_title = models.CharField(max_length=50)
    f_contents = models.TextField()
    f_date = models.DateTimeField('date published')
    f_short_intro = models.CharField(max_length=100)
    f_file = models.FileField()
    f_image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.f_title

class Boards(models.Model):
    b_type = models.ForeignKey(Board_menu , on_delete=models.CASCADE)
    f_id = models.ForeignKey(File, on_delete=models.CASCADE,null=True, blank=True)
    b_title = models.CharField(max_length=50)
    b_contents = models.TextField()
    b_images = models.ImageField(null=True, blank=True)
    b_date = models.DateTimeField('date published')
    b_short_intro = models.CharField(max_length=100)
    def __str__(self):
        return self.b_title


class SummerNote(summer_model.Attachment):
    summer_field = summer_fields.SummernoteTextField(default='')

