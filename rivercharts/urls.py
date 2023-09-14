# rivercharts URL Configuration (App Level)

from django.urls import path
from . import views

urlpatterns = [
    path('river-graph/', views.river_graph_initial, name='river-graph-initial'),    
    path('', views.river_graph_initial, name='river-graph-initial'),
    path('river-graph-data/', views.river_graph_data, name='river-graph-data'),
    path('error/', views.error_view, name='error_view'),
    path('error/<str:error_message>/', views.error_view, name='error_view_with_message'),
    
]

