from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import EquipmentDataset
from .utils import analyze_csv
from .serializers import EquipmentDatasetSerializer
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from rest_framework import status
from .serializers import CSVUploadSerializer

from .utils import analyze_csv, generate_dataset_pdf
from django.http import FileResponse


class UploadCSVView(APIView):
    parser_classes = [MultiPartParser]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CSVUploadSerializer

    def get(self, request):
        return Response({"detail": "GET method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        csv_file = request.FILES.get("csv_file")
        if not csv_file:
            return Response({"error": "No file uploaded"}, status=400)

        csv_file.seek(0)
        summary = analyze_csv(csv_file)
        csv_file.seek(0)

        EquipmentDataset.objects.create(
            csv_file=csv_file,
            user=request.user,  # mandatory now
            **summary
        )

        # Keep only last 5 datasets per user
        user_datasets = EquipmentDataset.objects.filter(user=request.user)
        if user_datasets.count() > 5:
            user_datasets.order_by('uploaded_at').first().delete()

        return Response(summary)
class DatasetHistoryView(APIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request):
        datasets = EquipmentDataset.objects.filter(user=request.user).order_by('-uploaded_at')[:5]
        serializer = EquipmentDatasetSerializer(datasets, many=True)
        return Response(serializer.data)
class GeneratePDFView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, dataset_id):
        try:
            dataset = EquipmentDataset.objects.get(id=dataset_id)
        except EquipmentDataset.DoesNotExist:
            return Response({"error": "Dataset not found"}, status=404)

        if dataset.user != request.user:
            return Response({"error": "Forbidden"}, status=403)

        analysis = {
            "total_equipment": dataset.total_equipment,
            "avg_flowrate": dataset.avg_flowrate,
            "avg_pressure": dataset.avg_pressure,
            "avg_temperature": dataset.avg_temperature,
            "type_distribution": dataset.type_distribution,
        }

        # Open CSV and generate chart data
        dataset.csv_file.open()
        dataset.csv_file.seek(0)
        analysis_csv = analyze_csv(dataset.csv_file)

        import pandas as pd
        df = pd.DataFrame(analysis_csv["table_data"])
        chart_data = {
            "Flowrate": df["flowrate"].tolist(),
            "Pressure": df["pressure"].tolist(),
            "Temperature": df["temperature"].tolist(),
        }

        pdf_buffer = generate_dataset_pdf(dataset, analysis, chart_data)

        return FileResponse(
            pdf_buffer,
            as_attachment=True,
            filename=f"dataset_{dataset_id}_report.pdf"
        )
