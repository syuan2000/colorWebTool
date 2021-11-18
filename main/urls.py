from django.urls import path, re_path
from . import views
from django.views.decorators.csrf import csrf_exempt

#map our URL pattern to the view functions
urlpatterns = [
    # path('<int:id>',views.index, name='index'),
    path('test/',views.test, name='test'),
    path('',views.home, name='home'),
    path('instruction/', views.instruction, name="instruction"),
    path('assessment/', views.assessment, name = 'assessment'),
    path('assessment/thankYou/', views.thankYou, name = 'thankYou'),
    re_path(r'^assessment_api/', csrf_exempt(views.assessment_api), name='assessment_api'),

    
]