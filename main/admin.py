from django.contrib import admin
from .models import PredictionHistory

@admin.register(PredictionHistory)
class PredictionHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'ph_input', 'tds_input', 'result', 'prediction_date')
    list_filter = ('user', 'result', 'prediction_date')
    search_fields = ('user__username', 'result')
