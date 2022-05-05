from django.contrib import admin
from .models import UploadModel
# Register your models here.
class UploadModelAdmin(admin.ModelAdmin):
      list_display = ('firstName', 'lastName','title','department','Fileupload')


admin.site.register(UploadModel,UploadModelAdmin)


