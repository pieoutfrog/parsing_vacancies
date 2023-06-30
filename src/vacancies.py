from src.api_class import JobFinder, HHJobFinder, SuperjobsJobFinder


class Vacancies:

    def __init__(self, url: str, salary, description: str, title: str, area: str, experience: str):
        self.url = url
        if salary is None or salary == '0' or 0:
            self.salary = 'Не указана'
        else:
            self.salary = salary
        self.salary = salary
        self.description = description
        self.title = title
        self.area = area
        self.experience = experience
        # self.validate()

    def validate(self):
        if not isinstance(self.title, str):
            raise ValueError("Название должно быть строкой")
        if not isinstance(self.url, str):
            raise ValueError("Ссылка должна быть строкой")
        if not isinstance(self.salary, (int, float)):
            raise ValueError("Зарплата должна быть цифровым значением")
        if not isinstance(self.description, str):
            raise ValueError("Описание должно быть строкой")

    def __str__(self):
        return f"""Название вакансии: {self.title}
Зарплата: {self.salary}
Требуемый опыт: {self.experience}
Описание: {self.description}
Ссылка на вакансию: {self.url}
Регион: {self.area}."""
