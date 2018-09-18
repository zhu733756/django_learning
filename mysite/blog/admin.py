from django.contrib import admin
from .models import Article,Person
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time')

    def save_model(self, request, obj, form, change):
        if change:  # 更改的时候
            obj_original = self.model.objects.get(pk=obj.pk)
        else:  # 新增的时候
            obj_original = None

        obj.user = request.user
        obj.save()

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ('name',)
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(PersonAdmin, self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(age=search_term_as_int)
        except:
            pass
        return queryset, use_distinct

class QuerysetAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs=super(QuerysetAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
# admin.site.register(QuerysetAdmin)