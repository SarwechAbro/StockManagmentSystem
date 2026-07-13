from django.urls import path
from . import views

urlpatterns = [
    path('items', views.ItemListCreateView.as_view(), name='item-list'),
    path('items/<int:id>', views.ItemRetrieveUpdateDestroyView.as_view(), name='item-detail'),

    path('categories', views.CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:id>', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),

    path('stocks', views.StockListCreateView.as_view(), name='stock-list'),
    path('stocks/<int:id>', views.StockRetrieveUpdateDestroyView.as_view(), name='stock-detail'),

    path('sections', views.SectionListCreateView.as_view(), name='section-list'),
    path('sections/<int:id>', views.SectionRetrieveUpdateDestroyView.as_view(), name='section-detail'),

    path('stockout', views.StockOutListCreateView.as_view(), name='stockout-list'),
    path('stockout/<int:id>', views.StockOutRetrieveUpdateDestroyView.as_view(), name='stockout-detail'),

    path('export-stockin-csv', views.export_stockin_csv, name='export-stockin-csv'),
    path('export-stockout-csv', views.export_stockout_csv, name='export-stockout-csv'),
    path('astrick/careers', views.test_view, name='test-view'),
]
