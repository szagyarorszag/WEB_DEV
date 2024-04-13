from django.contrib import admin
from django.urls import path
from views import *

urlpatterns = [
    path('companies/', get_companies),
    path('companies/<int:id>/', get_company_by_id),
    path('companies/<int:id>/vacancies/', get_vacancies_by_company),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:id>', VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten', VacancyTopTenAPIView.as_view()),
]
