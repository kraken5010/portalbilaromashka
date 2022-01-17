from django.contrib import admin
from django import forms
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


class Publish:
    # Добавление в поле "Действия дополнительных возможностей"
    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запис було оновлено'
        else:
            message_bit = f'{row_update} записів було оновлено'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запис було оновлено'
        else:
            message_bit = f'{row_update} записів було оновлено'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Опублікувати'
    publish.allowed_permissions = ('change',)

    unpublish.short_description = 'Зняти з публікації'
    unpublish.allowed_permissions = ('change',)


class ImageForAdmin:
    """Вывод изображения в админке"""
    def get_image(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='100' height='120'>")

    get_image.short_description = 'Фото'


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент', widget=CKEditorUploadingWidget())

    class Meta:
        model = CommercialArticle
        fields = '__all__'


class DepartmentAdmin(admin.ModelAdmin):
    """"Департаменты"""
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class CommercialArticleAdmin(admin.ModelAdmin, Publish):
    """"Статьи"""
    list_display = ('title', 'dep', 'time_create', 'draft')
    search_fields = ('title',)
    list_editable = ('draft',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish', 'unpublish']  # поля взяты из методов экшен ниже
    form = ArticleAdminForm
    readonly_fields = ('time_create',)


class CommercialStructureAdmin(admin.ModelAdmin, ImageForAdmin):
    """"Сотрудники офиса"""
    list_display = ('full_name', 'position', 'phone', 'email', 'get_image')
    search_fields = ('full_name',)
    readonly_fields = ('get_image',)


class OperationsArticleAdmin(admin.ModelAdmin, Publish):
    """"Статьи"""
    list_display = ('title', 'slug', 'time_create', 'draft')
    search_fields = ('title',)
    list_editable = ('draft',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish', 'unpublish']  # поля взяты из методов экшен ниже
    form = ArticleAdminForm
    readonly_fields = ('time_create',)


class OperationsStructureAdmin(admin.ModelAdmin, ImageForAdmin):
    """"Сотрудники офиса"""
    list_display = ('full_name', 'position', 'phone', 'email', 'get_image')
    search_fields = ('full_name',)
    readonly_fields = ('get_image',)


class FinancialArticleAdmin(admin.ModelAdmin, Publish):
    """"Статьи"""
    list_display = ('title', 'slug', 'time_create', 'draft')
    search_fields = ('title',)
    list_editable = ('draft',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish', 'unpublish']  # поля взяты из методов экшен ниже
    form = ArticleAdminForm
    readonly_fields = ('time_create',)


class FinancialStructureAdmin(admin.ModelAdmin, ImageForAdmin):
    """"Сотрудники офиса"""
    list_display = ('full_name', 'position', 'phone', 'email', 'get_image')
    search_fields = ('full_name',)
    readonly_fields = ('get_image',)


class AccountingArticleAdmin(admin.ModelAdmin, Publish):
    """"Статьи"""
    list_display = ('title', 'slug', 'time_create', 'draft')
    search_fields = ('title',)
    list_editable = ('draft',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish', 'unpublish']  # поля взяты из методов экшен ниже
    form = ArticleAdminForm
    readonly_fields = ('time_create',)


class AccountingStructureAdmin(admin.ModelAdmin, ImageForAdmin):
    """"Сотрудники офиса"""
    list_display = ('full_name', 'position', 'phone', 'email', 'get_image')
    search_fields = ('full_name',)
    readonly_fields = ('get_image',)


class DevelopmentArticleAdmin(admin.ModelAdmin, Publish):
    """"Статьи"""
    list_display = ('title', 'slug', 'time_create', 'draft')
    search_fields = ('title',)
    list_editable = ('draft',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish', 'unpublish']  # поля взяты из методов экшен ниже
    form = ArticleAdminForm
    readonly_fields = ('time_create',)


class DevelopmentStructureAdmin(admin.ModelAdmin, ImageForAdmin):
    """"Сотрудники офиса"""
    list_display = ('full_name', 'position', 'phone', 'email', 'get_image')
    search_fields = ('full_name',)
    readonly_fields = ('get_image',)


class ItArticleAdmin(admin.ModelAdmin, Publish):
    """"Статьи"""
    list_display = ('title', 'slug', 'time_create', 'draft')
    search_fields = ('title',)
    list_editable = ('draft',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish', 'unpublish']  # поля взяты из методов экшен ниже
    form = ArticleAdminForm
    readonly_fields = ('time_create',)
    save_on_top = True

class ItStructureAdmin(admin.ModelAdmin, ImageForAdmin):
    """"Сотрудники офиса"""
    list_display = ('full_name', 'position', 'phone', 'email', 'get_image')
    search_fields = ('full_name',)
    readonly_fields = ('get_image',)


class MarketingArticleAdmin(admin.ModelAdmin, Publish):
    """"Статьи"""
    list_display = ('title', 'slug', 'time_create', 'draft')
    search_fields = ('title',)
    list_editable = ('draft',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish', 'unpublish']  # поля взяты из методов экшен ниже
    form = ArticleAdminForm
    readonly_fields = ('time_create',)


class MarketingStructureAdmin(admin.ModelAdmin, ImageForAdmin):
    """"Сотрудники офиса"""
    list_display = ('full_name', 'position', 'phone', 'email', 'get_image')
    search_fields = ('full_name',)
    readonly_fields = ('get_image',)


class PersonnelArticleAdmin(admin.ModelAdmin, Publish):
    """"Статьи"""
    list_display = ('title', 'slug', 'time_create', 'draft')
    search_fields = ('title',)
    list_editable = ('draft',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish', 'unpublish']  # поля взяты из методов экшен ниже
    form = ArticleAdminForm
    readonly_fields = ('time_create',)


class PersonnelStructureAdmin(admin.ModelAdmin, ImageForAdmin):
    """"Сотрудники офиса"""
    list_display = ('full_name', 'position', 'phone', 'email', 'get_image')
    search_fields = ('full_name',)
    readonly_fields = ('get_image',)


class LeaderAdmin(admin.ModelAdmin, ImageForAdmin):
    """"Сотрудники офиса"""
    list_display = ('full_name', 'position', 'phone', 'email', 'get_image')
    search_fields = ('full_name',)
    readonly_fields = ('get_image',)


class MyAdminSite(AdminSite):
    """Изменение сортировки моделей в админке"""
    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        #for app in app_list:
        #    app['models'].sort(key=lambda x: x['name'])
        return app_list


admin.site = MyAdminSite()

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Leader, LeaderAdmin)
admin.site.register(CommercialArticle, CommercialArticleAdmin)
admin.site.register(CommercialStructure, CommercialStructureAdmin)
admin.site.register(OperationsArticle, OperationsArticleAdmin)
admin.site.register(OperationsStructure, OperationsStructureAdmin)
admin.site.register(FinancialArticle, FinancialArticleAdmin)
admin.site.register(FinancialStructure, FinancialStructureAdmin)
admin.site.register(AccountingArticle, AccountingArticleAdmin)
admin.site.register(AccountingStructure, AccountingStructureAdmin)
admin.site.register(DevelopmentArticle, DevelopmentArticleAdmin)
admin.site.register(DevelopmentStructure, DevelopmentStructureAdmin)
admin.site.register(ItArticle, ItArticleAdmin)
admin.site.register(ItStructure, ItStructureAdmin)
admin.site.register(MarketingArticle, MarketingArticleAdmin)
admin.site.register(MarketingStructure, MarketingStructureAdmin)
admin.site.register(PersonnelArticle, PersonnelArticleAdmin)
admin.site.register(PersonnelStructure, PersonnelStructureAdmin)


admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)

admin.site.site_title = 'Адмінка Portal Bilaromashka'
admin.site.site_header = 'Адмінка Portal Bilaromashka'


