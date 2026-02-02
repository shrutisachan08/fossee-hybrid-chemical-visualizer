from django.db import models
from django.contrib.auth.models import User

class EquipmentDataset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    uploaded_at = models.DateTimeField(auto_now_add=True)
    csv_file = models.FileField(upload_to='uploads/')

    total_equipment = models.IntegerField()
    avg_flowrate = models.FloatField()
    avg_pressure = models.FloatField()
    avg_temperature = models.FloatField()

    type_distribution = models.JSONField()
    table_data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"Dataset {self.id} uploaded at {self.uploaded_at}"

