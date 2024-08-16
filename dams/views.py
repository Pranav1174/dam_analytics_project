from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Dam, DamStatistics
from .serializers import DamSerializer, DamStatisticsSerializer

class DamViewSet(viewsets.ModelViewSet):
    queryset = Dam.objects.all()
    serializer_class = DamSerializer

class DamStatisticsViewSet(viewsets.ModelViewSet):
    queryset = DamStatistics.objects.all()
    serializer_class = DamStatisticsSerializer

    @action(detail=False, methods=['get'])
    def get_highest_rainfall(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        if not start_date or not end_date:
            return Response({'error': 'Please provide both start_date and end_date query parameters.'}, status=400)
        
        try:
            highest_rainfall = DamStatistics.objects.filter(date__range=[start_date, end_date]).order_by('-rainfall').first()
            return Response({'highest_rainfall': highest_rainfall.rainfall if highest_rainfall else 'No data'})
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @action(detail=True, methods=['get'])
    def get_date_of_highest_rainfall(self, request, pk=None):
        try:
            dam = Dam.objects.get(pk=pk)
            highest_rainfall = DamStatistics.objects.filter(dam=dam).order_by('-rainfall').first()
            return Response({'date': highest_rainfall.date if highest_rainfall else 'No data'})
        except Dam.DoesNotExist:
            return Response({'error': 'Dam not found'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @action(detail=False, methods=['get'])
    def list_dams_by_district(self, request):
        district = request.query_params.get('district')
        if not district:
            return Response({'error': 'Please provide the district query parameter.'}, status=400)
        
        try:
            dams = Dam.objects.filter(district=district)
            serializer = DamSerializer(dams, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)