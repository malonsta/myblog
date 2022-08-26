from django.contrib import admin
from myblog.models import Post, Category, Contact
from django.contrib.auth.models import Group, User


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact, ContactAdmin)
