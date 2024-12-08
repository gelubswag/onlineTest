from django.urls import path
from testApp.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "testApp"

urlpatterns = [
    path('test/', testpage, name="test"),    
    path('', main, name="main"),
    
    path('addSubject/', addSubject, name="addSubject"),
    path('deleteSubject/<int:subId>', deleteSubject, name="deleteSubject"),
    path('changeSubject/<int:subId>', changeSubject, name="changeSubject"),
    path('<int:subId>', detailsSubject, name="detailsSubject"),
    
    
    path('<int:subId>/add', addTest, name="addTest"),
    path('<int:subId>/delete/<int:testId>', deleteTest, name="deleteTest"),
    path('<int:subId>/change/<int:testId>', changeTest, name="changeTest"),
    path('<int:subId>/<int:testId>', detailsTest, name="detailsTest"),
    path('<int:subId>/<int:testId>/run', run_test, name="RunTest"),
    
    
    path('<int:subId>/<int:testId>/<int:questId>', detailsQuest, name="detailsQuest"),
    path('<int:subId>/<int:testId>/<int:questId>/opts', changeOpts, name="changeOpts"),
    path('<int:subId>/<int:testId>/<int:questId>/change', changeQuest, name='changeQuest'),
    path('<int:subId>/<int:testId>/<int:questId>/delete', deleteQuest, name='deleteQuest'),
    path('<int:subId>/<int:testId>/add', addQuest, name='addQuestion'),

    
    path('finishTest/<int:testId>', finishTest, name='finishTest'),
    
    path('userstat/', user_stat, name='userStat')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)