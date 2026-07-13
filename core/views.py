from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Item, category, section, StockIn, StockOut
from .serializers import ItemSerializer, CategorySerializer, SectionSerializer, StockSerializer, StockOutSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import csv
from datetime import datetime


#test view
@api_view(['GET'])
def test_view(request):
    username = request.COOKIES.get('username') or request.GET.get('username', 'there')
    return render(request, 'core/greetings.html', {'username': username})


#export stock csv
@api_view(['GET'])
def export_stockin_csv(request):
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    try:
        start_date = datetime.strptime(start_date_str, '%d/%m/%Y').date()
        end_date = datetime.strptime(end_date_str, '%d/%m/%Y').date()
    except (TypeError, ValueError):
        return Response({'error': 'Invalid or missing date format'}, status=400)

    queryset = StockIn.objects.filter(date_of_entry__range=(start_date, end_date))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="file_{start_date}_to_{end_date}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Item Name', 'Quantity', 'Date of Entry', 'Category', 'Reciever', 'Remarks'])  # adjust headers

    for obj in queryset:
        writer.writerow([obj.item, obj.quantity, obj.date_of_entry, obj.category, obj.reciever, obj.remarks])  # adjust fields

    return response

#stock out csv
@api_view(['GET'])
def export_stockout_csv(request):
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')
    
    try:
        start_date = datetime.strptime(start_date_str, '%d/%m/%Y').date()
        end_date = datetime.strptime(end_date_str, '%d/%m/%Y').date()
        print(start_date, end_date)
    except (TypeError, ValueError):
        return Response({'error': 'Invalid or missing date format'}, status=400)

    queryset = StockOut.objects.filter(date_of_entry__range=(start_date, end_date))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="file_{start_date}_to_{end_date}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Item', 'Quantity', 'Date of Issue' ,'Category', 'Section', 'Name of Employee', 'Remarks'])  # adjust headers

    for obj in queryset:
        writer.writerow([obj.item, obj.quantity , obj.date_of_issue, obj.section, obj.emp_name, obj.remarks])  # adjust fields

    return response

#item API views
@method_decorator(csrf_exempt, name='dispatch')
class ItemListCreateView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@method_decorator(csrf_exempt, name='dispatch')
class ItemRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'


#category API views
@method_decorator(csrf_exempt, name='dispatch')
class CategoryListCreateView(ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer

@method_decorator(csrf_exempt, name='dispatch')
class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


#stock API views
@method_decorator(csrf_exempt, name='dispatch')
class StockListCreateView(ListCreateAPIView):
    queryset = StockIn.objects.all()
    serializer_class = StockSerializer

@method_decorator(csrf_exempt, name='dispatch')
class StockRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = StockIn.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'id'


#section API views
@method_decorator(csrf_exempt, name='dispatch')
class SectionListCreateView(ListCreateAPIView):
    queryset = section.objects.all()
    serializer_class = SectionSerializer

@method_decorator(csrf_exempt, name='dispatch')
class SectionRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = section.objects.all()
    serializer_class = SectionSerializer
    lookup_field = 'id'


#stock out API views
@method_decorator(csrf_exempt, name='dispatch')
class StockOutListCreateView(ListCreateAPIView):
    queryset = StockOut.objects.all()
    serializer_class = StockOutSerializer
    
@method_decorator(csrf_exempt, name='dispatch')
class StockOutRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = StockOut.objects.all()
    serializer_class = StockOutSerializer
    lookup_field = 'id'    
