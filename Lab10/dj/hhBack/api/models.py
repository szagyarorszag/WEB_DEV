from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return f'ID: {self.id} NAME: {self.name}'

    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'city' : self.city,
            'address' : self.address
        }
    class Meta:
        app_label = 'api'
        verbose_name = 'Company',
        verbose_name_plural = 'Companies'

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='vacancies', default=1)

    def __str__(self):
        return f'ID: {self.id} NAME: {self.name} DESCRIPTION: {self.description} SALARY: {self.salary} COMPANY: {self.company_id}'

    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'salary' : self.salary,
            'company' : self.company_id.to_json()
        }

    class Meta:
        app_label = 'api'
        verbose_name = 'Vacancy',
        verbose_name_plural = 'Vacancies'

