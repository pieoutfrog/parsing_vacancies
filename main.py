from src.api_class import HHJobFinder, SuperjobsJobFinder
from src.vacancies import Vacancies

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
    sj_vacancies = sj_api.get_vacancies('python', 'Москва')
    all_vacancies = []
    for vacancies in hh_vacancies:
        if vacancies['salary'] is None:
            salary = 'Не указана'
        else:
            salary = vacancies['salary']['from']
        title = vacancies['name']
        url = vacancies['alternate_url']
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


    # for v in superjob_vacancies:
    #     if v['payment_from'] is int:
    #         salary = v['payment_from']
    #     else:
    #         if v['payment_from'] is not None:
    #             salary_from = v['payment_from']
    #             salary = f'от {salary_from}'
    #         else:
    #             salary = 'Не указана'
    #     description = v['candidat']
    #     title = v['profession']
    #     area = v['town']['title']
    #     experience = v['experience']['title']
    #     all_vacancies.append(Vacancies(url, salary, description, title, area, experience))
    # sorted_vacancies = sorted(all_vacancies, key=lambda v: v.salary, reverse=True)
    for v in all_vacancies:
        print(v)
