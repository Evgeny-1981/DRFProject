from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Lesson)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', )
    list_filter = ('name',)
    search_fields = ('name', )
