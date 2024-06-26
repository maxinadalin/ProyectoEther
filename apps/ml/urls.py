from django.urls import path

from .views import *


urlpatterns = [
    path('pre-procesamiento', PreProcesamientoView.as_view()),
    path('regresion-lineal', RegresionLinealView.as_view()),
    path('clasificacion', ClassificacionView.as_view()),
    path('regresion_logica', LogicRegressionView.as_view()),
    path('age_regresion_logica', AgeLogicRegressionView.as_view())
]