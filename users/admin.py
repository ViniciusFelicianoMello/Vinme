from django.contrib import admin
from users.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'birth_date', 'nationality')
    search_fields = ('user__username', 'first_name', 'last_name')
    list_filter = ('nationality',)
    ordering = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)
