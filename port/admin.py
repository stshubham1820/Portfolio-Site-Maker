from django.contrib import admin

# Register your models here.
from port.models import *
class userAdmin(admin.ModelAdmin):
    list_display = ('user_name','name','passion','facebook','instagram','linkidin','twitter','skype')
    def __str__(self) -> str:
        return self.user_name
admin.site.register(user_profile,userAdmin)
class userAbout(admin.ModelAdmin):
    list_display = ('user','job_profile','job_desc','Dob','age','website','degree','phone','email','city','Freelancer','about','clients','project','Hrs','Awards')
    def __str__(self) -> str:
        return self.user
admin.site.register(user_about,userAbout)
class rresume(admin.ModelAdmin):
    list_display = ('user','skill','skillpercentage','highereducationtitle','highereducationYear','highereducationName','highereducationDescription','primaryeducationtitle','primaryeducationYear','primaryeducationName','primaryeducationDescription','primaryWorktitle','primaryWorkYear','primaryWorkName','primaryWorkDescription','secondaryWorktitle','secondaryWorkYear','secondaryWorkName','secondaryWorkDescription')
    def __str__(self) -> str:
        return self.user
admin.site.register(resume,rresume)
class inter(admin.ModelAdmin):
    list_display = ('user','icon','intrest')
    def __str__(self) -> str:
        return self.user
admin.site.register(intrest,inter)
class client(admin.ModelAdmin):
    list_display = ('user','ClientName','ClientProfile','ClientWords','ClientImage')
    def __str__(self) -> str:
        return self.user
admin.site.register(testimonial,client)
class serve(admin.ModelAdmin):
    list_display = ('user','ServiceIcon','ServiceName','ServiceDiscription')
    def __str__(self) -> str:
        return self.user
admin.site.register(Service,serve)
class img(admin.ModelAdmin):
    list_display = ('User','Name','Category','Image')
    def __str__(self) -> str:
        return self.user
admin.site.register(Images,img)