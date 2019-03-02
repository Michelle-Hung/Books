from django.contrib import admin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin
from book.models import Book,Catalog,Rating,Like,UserProfile
# Register your models here.


class BookAdmin(ImportExportModelAdmin):
	list_display = ('catalog','name','score')
	
admin.site.register(Book,BookAdmin)
admin.site.register(Catalog)
admin.site.register(Rating)
admin.site.register(Like)
admin.site.register(UserProfile)