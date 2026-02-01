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

class UploadCSVView(APIView):
    parser_classes = [MultiPartParser]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CSVUploadSerializer
    def get(self, request):
        return Response(
            {"detail": "GET method not allowed"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
    def post(self, request):
        csv_file = request.FILES.get("csv_file")

        if not csv_file:
            return Response({"error": "No file uploaded"}, status=400)

        csv_file.seek(0)
        summary = analyze_csv(csv_file)
        csv_file.seek(0)

        EquipmentDataset.objects.create(
            csv_file=csv_file,
            **summary
        )

        # Keep only last 5 datasets
        if EquipmentDataset.objects.count() > 5:
            EquipmentDataset.objects.order_by('uploaded_at').first().delete()

        return Response(summary)
class DatasetHistoryView(APIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request):
        datasets = EquipmentDataset.objects.order_by('-uploaded_at')[:5]
        serializer = EquipmentDatasetSerializer(datasets, many=True)
        return Response(serializer.data)
class GeneratePDFView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EquipmentDatasetSerializer
    def get(self, request, dataset_id):
        dataset = EquipmentDataset.objects.get(id=dataset_id)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        p = canvas.Canvas(response)
        p.drawString(100, 800, "Chemical Equipment Report")

        y = 760
        p.drawString(100, y, f"Total Equipment: {dataset.total_equipment}")
        y -= 20
        p.drawString(100, y, f"Avg Flowrate: {dataset.avg_flowrate}")
        y -= 20
        p.drawString(100, y, f"Avg Pressure: {dataset.avg_pressure}")
        y -= 20
        p.drawString(100, y, f"Avg Temperature: {dataset.avg_temperature}")

        p.showPage()
        p.save()
        return response