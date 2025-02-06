import configuration as c
import requests


def get_all_products():
    response = requests.get(c.BASE_URL + c.PRODUCTS)
    return response


def get_single_product(id: int):
    response = requests.get(c.BASE_URL + c.PRODUCTS + str(id))
    return response

