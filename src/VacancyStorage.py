from abc import abstractmethod, ABC

import simplejson as json
from src.vacancies import Vacancies


class VacancyStorage(ABC):
    def __init__(self, filepath):
        self.filepath = filepath

    @abstractmethod
    def load_vacancies(self):
        pass

    @abstractmethod
    def save_vacancies(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JsonVacancyStorage(VacancyStorage):
    def __init__(self, filepath):
        super().__init__(filepath)
        self.vacancies = None
        self.load_vacancies()

    def load_vacancies(self):
        try:
            with open(self.filepath, "r") as f:
                self.vacancies = json.load(f)
        except FileNotFoundError:
            self.vacancies = []

    def save_vacancies(self):
        with open(self.filepath, "w") as f:
            json.dump(self.vacancies, f)

    def get_vacancies(self):
        return self.vacancies

    def add_vacancy(self, vacancy):
        self.vacancies.append(vacancy)
        self.save_vacancies()

    def delete_vacancy(self, vacancy):
        self.vacancies.remove(vacancy)
        self.save_vacancies()