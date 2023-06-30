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
    superjob_api = SuperjobsJobFinder('https://api.superjob.ru/')
    superjob_vacancies = superjob_api.get_vacancies('python', 'Москва')
    all_vacancies = []
    print(hh_vacancies)
    for vacancies in hh_vacancies:
        if vacancies['salary'] is None:
            salary = 'Не указана'
        else:
            if vacancies['salary']['to'] is None:
                salary = vacancies['salary']['from']
        salary = vacancies['salary']

        title = vacancies['name']
        url = vacancies['alternate_url']
        description = vacancies['snippet']
        area = vacancies['area']['name']
        experience = vacancies['experience']['name']
        all_vacancies.append(Vacancies(url, salary, description, title, area, experience))


    # for v in hh_vacancies:
    #     url = v['url']
    #     if v['salary'] is int:
    #         salary = v['salary']
    #     else:
    #         if v['salary'] is not None:
    #             salary_from = v['salary']['from']
    #             salary = f'от {salary_from}'
    #         else:
    #             salary = 'Не указана'
    #     description = "{requirement} {responsibility}".format(**v['snippet'])
    #     title = v['name']
    #     area = v['area']['name']
    #     experience = v['experience']['name']
    #     all_vacancies.append(Vacancies(url, salary, description, title, area, experience))
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
