import requests
import json
from abc import ABC, abstractmethod
import os


class API(ABC):
    """Создание экземпляра абстрактного класса"""

    def __init__(self, api_key):
        self.__api_key = api_key

    @abstractmethod
    def get_vacancies(self, query, location):
        """Создание абстратного метода, получающего вакансии
        :param query: поисковой запрос для работы с вакансиями, который передается в параметре q в url.
        :param location: местоположение, где пользователь ищет работу, которое передается в параметре location в url.
        """
        pass


class HeadHunterAPI(API):

    api_key: str = os.getenv('HH_API_KEY')

    def __init__(self, api_key):
        """Наследование инит от супер-класса, инициализация базовой ссылки"""
        super().__init__(api_key)
        self.base_url = 'https://api.hh.ru/'

    def get_vacancies(self, query, location):
        """Метод, получающий вакансии из ссылки и возврающий вакансии в формате json"""
        url = f"{self.base_url}?text={query}&area={location}&per_page={20}&page={0}"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        vacancies = response.json()['items']
        return vacancies


class SuperJobAPI(API):

    api_key: str = os.getenv('SJ_API_KEY')

    def __init__(self, api_key):
        """Наследование инит от супер-класса, инициализация базовой ссылки"""
        super().__init__(api_key)
        self.base_url = 'https://superjobs.ru/vacancies'

    def get_vacancies(self, query, location):
        """Метод, получающий вакансии из ссылки и возврающий вакансии в формате json"""
        url = f"{self.base_url}?keywords={query}&location={location}&per_page={20}&page={0}"
        response = requests.get(url)
        vacancies = response.json()['offers']
        return vacancies
