from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

def get_companies(request):
    try:
        companies = Company.objects.all()
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Companies not found'}, status=404)
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)

def get_company_by_id(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)
    company_json = company.to_json()
    return JsonResponse(company_json, safe=False)

def get_vacancies_by_company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)
    try:
        vacancies = company.vacancies.all()
    except vacancies.DoesNotExist:
        return JsonResponse({'error': 'Vacancies not found'}, status=400)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)
def get_vacancies(request):
    try:
        vacancies = Vacancy.objects.all()
    except Vacancy.DoesNotExist:
        return JsonResponse({'error': 'Vacancies not found'}, status=404)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def get_vacancy_by_id(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        return JsonResponse({'error': 'Vacancy not found'}, status=404)
    vacancy_json = vacancy.to_json()
    return JsonResponse(vacancy_json, safe=False)


def get_top_ten_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)
