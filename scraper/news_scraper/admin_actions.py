import csv
from django.http import HttpResponse

def export_as_csv_action(description="Export selected objects as CSV file",
                         fields=None, exclude=None, header=True):
    """
    This function returns an export csv action
    'fields' and 'exclude' work like in django ModelForm
    'header' is whether or not to output the column names as the first row
    """
    def export_as_csv(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        
        if not fields:
            field_names = [field.name for field in opts.fields]
        else:
            field_names = fields

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % str(opts).replace('.', '_')

        writer = csv.writer(response)
        if header:
            writer.writerow(field_names)
        for obj in queryset:
            row = [getattr(obj, field)() if callable(getattr(obj, field)) else getattr(obj, field) for field in field_names]
            writer.writerow(row)
        return response
    export_as_csv.short_description = description
    return export_as_csv

def export_as_txt_action(description, fields=None, exclude='None'):
	"""
	Exports data into a txt file.
	"""
	def export_as_txt(modeladmin, request, queryset):
		opts = modeladmin.model._meta

		if not fields:
			field_names = [field.name for field in opts.fields if not(field.name in exclude)]
		else:
			field_names = fields

		response = HttpResponse(content_type='text/plain')
		response['Content-Disposition'] = 'attachment; filename=%s.txt' % str(opts).replace('.','_')

		for obj in queryset:
			line = ','
			line = line.join(str(getattr(obj, field)()) if callable(getattr(obj, field)) else str(getattr(obj, field)) for field in field_names)
			line = line + ' | '
			response.write(line)
		return response
	export_as_txt.description = description
	return export_as_txt

