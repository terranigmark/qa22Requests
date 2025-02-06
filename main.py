import configuration as c
import requests


def get_all_products():
    response = requests.get(c.BASE_URL + c.PRODUCTS)
    return response

