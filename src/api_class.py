import os
from abc import ABC, abstractmethod
from typing import List

import requests


class JobFinder(ABC):
    """
    Абстрактный класс для работы с API сайтов поиска работы
    """

    @abstractmethod
    def get_vacancies(self, query: str, location: str) -> List[dict]:
        """
        Абстрактный метод для получения вакансий
        :param query: строка поискового запроса
        :param location: строка локации
        :return: список словарей (вакансий)
        """
        pass


class HHJobFinder(JobFinder):
    """
    Класс для работы с API сайта hh.ru
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def get_vacancies(self, query: str, location: str) -> List[dict]:
        """
        Метод для получения вакансий с сайта hh.ru
        :param query: строка поискового запроса
        :param location: строка локации
        :return: список словарей (вакансий)
        """
        url = f"{self.base_url}?text={query}&area={location}&per_page={20}&page={0}"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        vacancies = response.json()['items']
        return vacancies


class SuperjobsJobFinder(JobFinder):
    """
    Класс для работы с API сайта superjobs
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def get_vacancies(self, query: str, location: str):
        # -> List[dict]:
        """
        Метод для получения вакансий с сайта superjobs.ru
        :param query: строка поискового запроса
        :param location: строка локации
        :return: список словарей (вакансий)
        """
        api_key: str = os.getenv('SJ_API_KEY')
        headers = {'X-Api-App-Id': api_key}
        url = f"{self.base_url}2.0/vacancies/"
        params = {
            'keyword': query,
            'town': location,
        }
        response = requests.get(url, headers=headers, params=params)
        vacancies = response.json()['objects']
        return vacancies
