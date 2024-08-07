from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Movie
from .resources import MovieResource

@admin.register(Movie)
class MovieAdmin(ImportExportModelAdmin):
    list_display = ['title', 'genre', 'rating', 'director', 'language']
    search_fields = ['title', 'genre', 'cast', 'language', 'isbn', 'director']
    list_filter = ['genre', 'rating', 'language']
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ['rating', 'language']
    list_display_links = ['title']
    ordering = ['title']
    fieldsets = [
        ('Movie Information', {'fields': ['title', 'genre', 'director', 'rating']}),
        ('Additional Details', {'fields': ['cast', 'language', 'isbn']}),
    ]
    resource_class = MovieResource
    readonly_fields = ['isbn']  # Example: make ISBN read-only if it shouldn't be edited
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=movies.csv'
        
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = 'Export selected movies as CSV'
