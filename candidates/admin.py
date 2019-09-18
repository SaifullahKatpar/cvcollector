from django.contrib import admin

# Register your models here.
from .models import User, Job, Candidate

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass
