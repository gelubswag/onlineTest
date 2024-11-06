from django.urls import path
from testApp.views import *
app_name = "testApp"

urlpatterns = [
    path('test/', testpage, name="test"),    
    path('', main, name="main"),
    path('addSubject/', addSubject, name="addSubject"),
    path('deleteSubject/<int:subId>', deleteSubject, name="deleteSubject"),
    path('changeSubject/<int:subId>', changeSubject, name="changeSubject"),
    path('<int:subId>', detailsSubject, name="detailsSubject")    
]
