import tempfile
import json
from src.api_class import HHJobFinder, SuperjobsJobFinder
from src.vacancies import Vacancies
from src.VacancyStorage import JsonVacancyStorage

# if __name__ == '__main__':
#     hh_api = HHJobFinder('https://api.hh.ru/vacancies')
#     hh_vacancies = hh_api.get_vacancies('python', '1')
#     print(hh_vacancies)
#
#     superjob_api = SuperjobsJobFinder('https://api.superjob.ru/')
#     superjob_vacancies = superjob_api.get_vacancies('python', 'Москва')
#     print(superjob_vacancies)
if __name__ == "__main__":
    hh_api = HHJobFinder('https://api.hh.ru/vacancies')
    hh_vacancies = hh_api.get_vacancies('python', '1')
    sj_api = SuperjobsJobFinder('https://api.superjob.ru/')
    sj_vacancies = sj_api.get_vacancies('python', 'Владивосток')
    all_vacancies = []
    for vacancies in hh_vacancies:
        if vacancies['salary'] is None:
            salary = 0
        else:
            salary = vacancies['salary']['from']
        title = vacancies['name']
        url = vacancies['alternate_url']
        if vacancies['snippet']['responsibility'] is None:
            description = """\nТребования: {requirement}\nОбязанности: отсутствуют""".format(
                **vacancies['snippet'])
        description = """\nТребования: {requirement}\nОбязанности: {responsibility}""".format(**vacancies['snippet'])
        area = vacancies['area']['name']
        experience = vacancies['experience']['name']
        all_vacancies.append(Vacancies(url, salary, description, title, area, experience))
    for vacancies in sj_vacancies:
        if vacancies['payment_from'] is None:
            salary = 'Не указана'
        else:
            salary = vacancies['payment_from']
        title = vacancies['profession']
        url = vacancies['client']['link']
        description = vacancies['candidat']
        area = vacancies['town']['title']
        experience = vacancies['experience']['title']
        all_vacancies.append(Vacancies(url, salary, description, title, area, experience))
        sorted_vacancies = sorted(all_vacancies, key=lambda x: x.salary, reverse=True)
        for v in sorted_vacancies:
            print(v)
            vacancy = JsonVacancyStorage.save_vacancies(v)


        storage = JsonVacancyStorage("vacancies.json")
        #
        # # Получаем список всех вакансий из файла и выводим его в консоль
        # all_vacancies = storage.get_vacancies()
        # for vacancy in all_vacancies:
        #     print(vacancy.url, vacancy.salary, vacancy.title, vacancy.area, vacancy.experience, vacancy.description,
        #           vacancy.datetime)
        #
        # # Получаем список вакансий в Москве из файла и выводим его в консоль
        # vdk_vacancies = storage.get_vacancies()
        # for vacancy in vdk_vacancies:
        #     print(vacancy.url, vacancy.salary, vacancy.title, vacancy.area, vacancy.experience, vacancy.description,
        #           vacancy.datetime)
