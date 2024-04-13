from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, Vacancy

from .serializer import CompanySerializer, VacancySerializer
#

@api_view(["GET"])
def get_companies(request):
    if request.method == "GET":
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_company_by_id(request, id=None):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        serializer = CompanySerializer(company)
        return Response(serializer.data)


@api_view(["GET"])
def get_vacancies_by_company(request, id=None):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        vacancies = Vacancy.objects.filter(company=company)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

class VacancyListAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)


class VacancyDetailAPIView(APIView):
    def get_object(self, pk=None):
        try:
            vacancy = Vacancy.objects.get(id=pk)
            return vacancy
        except Vacancy.DoesNotExist as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        vacancy = self.get_object(id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)


class VacancyTopTenAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.order_by("-salary")
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
