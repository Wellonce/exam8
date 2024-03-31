from django.shortcuts import render
from .models import Vacancy

def homeView(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'home.html', {"vacancies": vacancies})

def filter_vacancies(salary_from=None, salary_to=None, salary=None):
    vacancies = Vacancy.objects.all()

    if salary_from:
        vacancies = vacancies.filter(salary__gte=salary_from)

    if salary_to:
        vacancies = vacancies.filter(salary__lte=salary_to)

    if salary:
        vacancies = vacancies.filter(salary=salary)

    return vacancies

def search_vacancies(request):
    salary_from = request.GET.get('salary_from')
    salary_to = request.GET.get('salary_to')
    salary = request.GET.get('salary')

    vacancies = []  

    if salary_from or salary_to or salary:
        vacancies = filter_vacancies(salary_from, salary_to, salary)

    return render(request, 'vacancy_search.html', {'vacancies': vacancies, 'salary_from': salary_from, 'salary_to': salary_to, 'salary': salary})



