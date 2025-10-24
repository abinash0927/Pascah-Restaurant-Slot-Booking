from django.urls import path
from .views import Homepage,Bookpage,ListView,ListupdateView,ListTableView

urlpatterns = [
    path('',Homepage,name='home'),
    path('slot/',Bookpage,name='book'),
    path('owner/',ListView.as_view()),
    path('user/',ListTableView.as_view()),
    path('user/<int:table>/',ListupdateView.as_view())
]