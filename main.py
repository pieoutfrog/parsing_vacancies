
import json
from src.api_class import HHJobFinder, SuperjobsJobFinder
from src.VacancyStorage import JsonVacanciesFile

if __name__ == "__main__":
    hh_api = HHJobFinder('https://api.hh.ru/vacancies')
    hh_vacancies = hh_api.get_vacancies('python', '1')
    sj_api = SuperjobsJobFinder('https://api.superjob.ru/')
    sj_vacancies = sj_api.get_vacancies('python', 'Россия')
    storage = JsonVacanciesFile('vacancies.json')
    all_vacancies = [
                        {
                            'url': vacancies['alternate_url'],
                            'salary': vacancies['salary']['from'] if vacancies['salary'] else None,
                            'description': """\nТребования: {requirement}\nОбязанности: {responsibility}""".format(
                                **vacancies['snippet']) if vacancies['snippet'][
                                'responsibility'] else """\nТребования: {requirement}\nОбязанности: отсутствуют""".format(
                                **vacancies['snippet']),
                            'title': vacancies['name'],
                            'area': vacancies['area']['name'],
                            'experience': vacancies['experience']['name']
                        } for vacancies in hh_vacancies if vacancies['salary'] is not None
                    ] + [
                        {
                            'url': vacancies['client']['link'],
                            'salary': vacancies['payment_from'],
                            'description': vacancies['candidat'],
                            'title': vacancies['profession'],
                            'area': vacancies['town']['title'],
                            'experience': vacancies['experience']['title']
                        } for vacancies in sj_vacancies if vacancies['payment_from'] is not None
                    ]

    storage.save_vacancies(all_vacancies)
    for vacancy in all_vacancies:

       sorted_vacancies = sorted(vacancy.items(), key=lambda x: x['salary'])
    print(sorted_vacancies)
    # def interactive_menu():
    #     # создаем экземпляр класса для работы с файлом вакансий в формате JSON
    #     vacancies_file = JsonVacanciesFile('vacancies.json')
    #
    #     while True:
    #         # выводим меню
    #         print('Меню:')
    #         print('1. Получить вакансии с указанных платформ')
    #         print('2. Найти вакансии по ключевым словам в описании')
    #         print('3. Получить топ N вакансий по зарплате')
    #         print('4. Получить вакансии в отсортированном виде')
    #         print('5. Выход')
    #
    #         # запрашиваем у пользователя выбранный пункт меню
    #         choice = input('Введите номер пункта меню: ')
    #
    #         if choice == '1':
    #             # запрашиваем у пользователя платформы, с которых нужно получить вакансии
    #             platforms = input('Введите через запятую платформы: ')
    #             platforms = [x.strip() for x in platforms.split(',')]
    #             # получаем вакансии с указанных платформ
    #             vacancies = vacancies_file.get_vacancies(platform__in=platforms)
    #             # выводим вакансии на экран
    #             print(vacancies)
    #
    #         elif choice == '2':
    #             # запрашиваем у пользователя ключевые слова для поиска
    #             keywords = input('Введите ключевые слова через запятую: ')
    #             keywords = [x.strip() for x in keywords.split(',')]
    #             # получаем вакансии с указанными ключевыми словами в описании
    #             vacancies = vacancies_file.get_vacancies(description__contains=keywords)
    #             # выводим вакансии на экран
    #             print(vacancies)
    #
    #         elif choice == '3':
    #             # запрашиваем у пользователя, сколько вакансий нужно вывести
    #             n = int(input('Сколько вакансий вывести?: '))
    #             # получаем топ N вакансий по зарплате
    #             vacancies = vacancies_file.get_vacancies(order_by=('-salary_max',))[:n]
    #             # выводим вакансии на экран
    #             print(vacancies)
    #
    #         elif choice == '4':
    #             # получаем вакансии в отсортированном виде
    #             vacancies = vacancies_file.get_vacancies(order_by=('salary_max', 'published_at'))
    #             # выводим вакансии на экран
    #             print(vacancies)
    #
    #         elif choice == '5':
    #             # выходим из программы
    #             break
    #
    #         else:
    #             # если пользователь ввел некорректный пункт меню
    #             print('Некорректный выбор меню')
    #
    #
    # interactive_menu()