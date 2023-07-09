import json
from src.api_class import HHJobFinder, SuperjobsJobFinder
from src.VacancyStorage import JsonVacanciesFile
from src.vacancies import Vacancies

if __name__ == "__main__":
    """
    first_step позволяет пользователю выбрать, какую вакансию он ищет по атрибуту query
    Создаются экземпляры класса, получающие вакансии с платформ
    """
    first_step = input('Какую профессию ищем?').lower()
    hh_api = HHJobFinder('https://api.hh.ru/vacancies')
    hh_vacancies = hh_api.get_vacancies(first_step)
    sj_api = SuperjobsJobFinder('https://api.superjob.ru/')
    sj_vacancies = sj_api.get_vacancies(first_step)
    """
    all_vacancies - это список словарей с данными с двух платформ, позволяющий внести все вакансии в единый объект
    """
    all_vacancies = [
                        {
                            'url': vacancies['alternate_url'],
                            'platform': 'hh.ru',
                            'salary': vacancies['salary']['from'],
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
                            'url': vacancies['link'],
                            'platform': 'superjob.ru',
                            'salary': vacancies['payment_from'],
                            'description': vacancies['candidat'],
                            'title': vacancies['profession'],
                            'area': vacancies['town']['title'],
                            'experience': vacancies['experience']['title']
                        } for vacancies in sj_vacancies if vacancies['payment_from'] is not None
                    ]


    def interactive_menu():
        """
        Функция работы с пользователем
        Создается экземпляр класса JsonVacanciesFile для создания json-файла и последующей записи в него данных
        """
        vacancies_file = JsonVacanciesFile('vacancies.json')
        """
        Сортировка вакансий в списке словарей по зарплате от большей к меньшей 
        и запись отсортированных вакансий в json-файл
        """
        sorted_vacancies = sorted(all_vacancies, key=lambda d: d['salary'] if d['salary'] is not None else 0,
                                  reverse=True)
        vacancies_file.save_vacancies(sorted_vacancies)
        while True:
            # выводим меню
            print('Меню:')
            print('1. Получить вакансии с указанных платформ')
            print('2. Найти вакансии по ключевым словам в описании')
            print('3. Получить топ N вакансий по зарплате')
            print('4. Выход')

            # запрашиваем у пользователя выбранный пункт меню
            choice = input('Введите номер пункта меню: ')

            if choice == '1':
                # запрашиваем у пользователя платформы, с которых нужно получить вакансии
                platforms = input('Введите через запятую платформы: ').lower()
                platforms = [x.strip() for x in platforms.split(',')]
                # получаем вакансии с указанных платформ
                vacancies = vacancies_file.get_vacancies(platform=platforms, f='in')
                for v in vacancies:
                    print(v)

            elif choice == '2':
                # запрашиваем у пользователя ключевые слова для поиска
                keywords = input('Введите ключевые слова через запятую: ')
                keywords = [x.strip() for x in keywords.split(',')]
                # получаем вакансии с указанными ключевыми словами в описании
                vacancies = vacancies_file.get_vacancies(description=keywords, f='contains')
                for v in vacancies:
                    print(v)

            elif choice == '3':
                # запрашиваем у пользователя, сколько вакансий нужно вывести
                n = int(input('Сколько вакансий вывести?: '))
                # получаем топ N вакансий по зарплате
                vacancies = vacancies_file.get_vacancies()
                # выводим вакансии на экран
                for v in vacancies[:n]:
                    print(v)

            elif choice == '4':
                # выходим из программы
                break

            else:
                # если пользователь ввел некорректный пункт меню
                print('Некорректный выбор меню')


    interactive_menu()
