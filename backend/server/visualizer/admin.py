from django.contrib import admin
from .models import EquipmentDataset

@admin.register(EquipmentDataset)
class EquipmentDatasetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'uploaded_at',
        'csv_file',
        'total_equipment',
        'avg_flowrate',
        'avg_pressure',
        'avg_temperature',
         )

    readonly_fields = (
        "uploaded_at",
        "total_equipment",
        "avg_flowrate",
        "avg_pressure",
        "avg_temperature",
        "type_distribution",
    )

    fields = (
        "csv_file",
        "uploaded_at",
        "total_equipment",
        "avg_flowrate",
        "avg_pressure",
        "avg_temperature",
        "type_distribution",
    )
