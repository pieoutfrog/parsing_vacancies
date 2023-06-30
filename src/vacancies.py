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

    def __str__(self):
        return f"""Название вакансии: {self.title}
        Зарплата: {self.salary}
        Требуемый опыт: {self.experience}
        Описание: {self.description}
        Ссылка на вакансию: {self.url}
        Регион: {self.area}."""
