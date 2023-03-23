from django.contrib import admin
from .models import Student, AudioFile, Score
import csv
from django.http import HttpResponse

class EvaldataInline(admin.StackedInline):
    model = AudioFile
    extra = 2

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = (EvaldataInline,)
    list_display_links = ['id', 'name']
    list_display = ('id', 'name')

@admin.register(AudioFile)
class AudioFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_number', 'item_type', 'eval_component', 'item_text', 'audio_file', 'uploaded_at')
    list_display_links = ['id', 'student_number']
    list_filter = ('id', 'student_number', 'uploaded_at')
    ordering = ['id', 'student_number', 'item_type', 'eval_component', 'item_text', 'audio_file', 'uploaded_at']
    readonly_fields = ['uploaded_at']

    def export_to_excel(self, request, queryset):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="audio_files.csv"'

        writer = csv.writer(response)
        writer.writerow(
            ['id', 'student_number', 'item_type', 'eval_component', 'item_text', 'audio_file', 'uploaded_at'])

        for obj in queryset:
            writer.writerow(
                [obj.id, obj.student_number, obj.item_type, obj.eval_component, obj.item_text, obj.audio_file,
                 obj.uploaded_at])

        return response

    export_to_excel.short_description = 'Export selected to Excel'

    actions = [export_to_excel]

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display_links = ['id', 'user', 'student', 'eval_item', 'rating_un', 'rating_fu', 'rating_ac',
                          'rating_ph', 'rating_accent', 'rating_rule', 'rating_speed', 'rating_pause']
    list_display = ('id', 'user', 'student', 'eval_item', 'rating_un', 'rating_fu', 'rating_ac',
                    'rating_ph', 'rating_accent', 'rating_rule', 'rating_speed', 'rating_pause')
    ordering = ['id', 'user', 'student', 'eval_item', 'rating_un', 'rating_fu', 'rating_ac',
                'rating_ph', 'rating_accent', 'rating_rule', 'rating_speed', 'rating_pause']

    def export_to_excel(self, request, queryset):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="eval_score.csv"'

        writer = csv.writer(response)
        writer.writerow(
            ['id', 'user', 'student', 'eval_item',
             'rating_un', 'rating_fu', 'rating_ac',
             'rating_ph', 'rating_accent', 'rating_rule', 'rating_speed', 'rating_pause'])

        for obj in queryset:
            writer.writerow(
                [obj.id, obj.user, obj.student, obj.eval_item,
                 obj.rating_un, obj.rating_fu, obj.rating_ac,
                 obj.rating_ph, obj.rating_accent, obj.rating_rule, obj.rating_speed, obj.rating_pause])

        return response

    export_to_excel.short_description = 'Export selected to Excel'

    actions = [export_to_excel]