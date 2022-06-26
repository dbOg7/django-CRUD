from django.urls import path
from app import views

urlpatterns = [
    path('',views.ListView.as_view(template_name='listview.html'), name="listview"),
    path('create/',views.CreateView.as_view(template_name='createview.html'), name="createview"),
    path('<int:pk>/',views.ReadView.as_view(template_name='readview.html'), name="detailview"),
    path('<int:pk>/update/',views.UpdateView.as_view(template_name='updateview.html'), name="updateview"),
    path('<int:pk>/delete/',views.DeleteView.as_view(template_name='deleteview.html'), name="deleteview"),
]
