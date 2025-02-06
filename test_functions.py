import configuration as c
import requests


def get_all_products():
    response = requests.get(c.BASE_URL + c.PRODUCTS)
    return response


def get_single_product(id: int):
    response = requests.get(c.BASE_URL + c.PRODUCTS + str(id))
    return response


def create_product(product_body):
    response = requests.post(c.BASE_URL + c.PRODUCTS, json=product_body)
    return response


def update_product(id: int, updated_body):
    response = requests.put(c.BASE_URL + c.PRODUCTS + str(id), json=updated_body)
    return response