from django.contrib import admin
from .models import *
from .admin_actions import *

#ModelAdmin classes.

class HeadlineAdmin(admin.ModelAdmin):
	date_hierarchy = 'scanned_date'
	list_display = ('scanned_date', 'text')
	list_filter = ('scanned_date',)
	search_fields = ['scanned_date', 'text']
	actions = [export_as_csv_action('CSV Export', fields=['scanned_date', 'text']), export_as_txt_action('Single-day txt export', fields=['text'])]

class IndexValueAdmin(admin.ModelAdmin):
	date_hierarchy = 'scanned_date'
	list_display = ('scanned_date', 'value')
	list_filter = ('scanned_date',)
	search_fields = ['scanned_date']
	actions = [export_as_csv_action('CSV Export', fields=['scanned_date', 'value'])]

# Register your models here.
admin.site.register(Headline, HeadlineAdmin)
admin.site.register(index_value, IndexValueAdmin)
