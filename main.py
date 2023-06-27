from src.api_class import HeadHunterAPI, SuperJobAPI

if __name__ == '__main__':
    hh_api = HeadHunterAPI('')
    r = hh_api.get_vacancies('', '')

