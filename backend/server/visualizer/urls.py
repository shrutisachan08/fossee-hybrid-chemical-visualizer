from django.urls import path
from .views import UploadCSVView, DatasetHistoryView,  GeneratePDFView

urlpatterns = [
    path('upload/', UploadCSVView.as_view()),
    path('history/', DatasetHistoryView.as_view()),
       path("datasets/<int:dataset_id>/report/", GeneratePDFView.as_view(), name="generate-pdf"),
]
