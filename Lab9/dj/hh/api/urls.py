from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('companies', get_companies),
    path('companies/<int:id>/', get_company_by_id),
    path('companies/<int:id>/vacancies/', get_vacancies_by_company),
    path('vacancies/', get_vacancies),
    path('vacancies/<int:id>/', get_vacancy_by_id),
    path('vacancies/top_ten/', get_top_ten_vacancies),
]
