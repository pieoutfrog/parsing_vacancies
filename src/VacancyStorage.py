import abc
import json
from src.vacancies import Vacancies


class VacanciesFile(abc.ABC):
    """
    Абстрактный класс, реализующий абстрактные методы, которые сохраняют, получают и удаляют вакансии
    """

    @abc.abstractmethod
    def save_vacancies(self, vacancies):
        pass

    @abc.abstractmethod
    def get_vacancies(self, **criteria):
        pass

    @abc.abstractmethod
    def delete_vacancies(self, **criteria):
        pass


class JsonVacanciesFile(VacanciesFile):
    """
    Класс, работающий с json-файлами
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def save_vacancies(self, vacancies):
        """
        Метод, записывающий вакансии в json-файл
        :param vacancies: вакансии
        """
        with open(self.file_path, 'w') as f:
            json.dump(vacancies, f, ensure_ascii=False)

    def get_vacancies(self, **criteria):
        """
        Метод, получающий вакансии по указанным критериям
        :param criteria: критерии, указанный пользователем
        :return: список вакансий, подобранных по указанному критерию
        """
        with open(self.file_path, 'r') as f:
            vacancies = json.load(f)
        result = []
        f = criteria.get('f')
        if f is None:
            for vacancy in vacancies:
                # Проверяем, соответствует ли вакансия критериям поиска
                if all(getattr(vacancy, key) == value for key, value in criteria.items()):
                    result.append(
                        Vacancies(url=vacancy['url'], salary=vacancy['salary'], description=vacancy['description'],
                                  title=vacancy['title'], area=vacancy['area'], experience=vacancy['experience']))
        else:
            criteria.pop('f')
            if f == 'in':
                for vacancy in vacancies:
                    # Проверяем, соответствует ли вакансия критериям поиска
                    if all(vacancy.get(key) in value for key, value in criteria.items()):
                        result.append(
                            Vacancies(url=vacancy['url'], salary=vacancy['salary'], description=vacancy['description'],
                                      title=vacancy['title'], area=vacancy['area'], experience=vacancy['experience']))
            elif f == 'contains':
                for vacancy in vacancies:
                    # Проверяем, соответствует ли вакансия критериям поиска
                    if all(any(v in vacancy.get(key) for v in value) for key, value in criteria.items()):
                        result.append(
                            Vacancies(url=vacancy['url'], salary=vacancy['salary'], description=vacancy['description'],
                                      title=vacancy['title'], area=vacancy['area'], experience=vacancy['experience']))
        return result

    def delete_vacancies(self, **criteria):
        """
        Метод, получающий список вакансий, подобранных по указанному критерию, которые нужно удалить
        :param criteria: критерий, указанный пользователем
        """
        with open(self.file_path, 'r') as f:
            vacancies = json.load(f)
        result = []
        f = criteria.get('f')
        criteria.pop('f')
        if f == 'in':
            for vacancy in vacancies:
                # Проверяем, соответствует ли вакансия критериям поиска
                if not all(vacancy.get(key) in value for key, value in criteria.items()):
                    result.append(
                        Vacancies(url=vacancy['url'], salary=vacancy['salary'], description=vacancy['description'],
                                  title=vacancy['title'], area=vacancy['area'], experience=vacancy['experience']))
        elif f == 'contains':
            for vacancy in vacancies:
                # Проверяем, соответствует ли вакансия критериям поиска
                if not all(any(v in vacancy.get(key) for v in value) for key, value in criteria.items()):
                    result.append(
                        Vacancies(url=vacancy['url'], salary=vacancy['salary'], description=vacancy['description'],
                                  title=vacancy['title'], area=vacancy['area'], experience=vacancy['experience']))
        with open(self.file_path, 'w') as f:
            json.dump(result, f, ensure_ascii=False)
