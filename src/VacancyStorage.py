import abc
import json


class VacanciesFile(abc.ABC):
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
    def __init__(self, file_path):
        self.file_path = file_path

    def save_vacancies(self, vacancies):
        with open(self.file_path, 'w') as f:
            json.dump(vacancies, f, ensure_ascii=False)

    def get_vacancies(self, **criteria):
        with open(self.file_path, 'r') as f:
            vacancies = json.load(f)
        result = []
        for vacancy in vacancies:
            # Проверяем, соответствует ли вакансия критериям поиска
            if all(getattr(vacancy, key) == value for key, value in criteria.items()):
                result.append(vacancy)
        return result

    def delete_vacancies(self, **criteria):
        with open(self.file_path, 'r') as f:
            vacancies = json.load(f)
        result = []
        for vacancy in vacancies:
            # Проверяем, соответствует ли вакансия критериям удаления
            if not all(getattr(vacancy, key) == value for key, value in criteria.items()):
                result.append(vacancy)
        with open(self.file_path, 'w') as f:
            json.dump(result, f, ensure_ascii=False)
