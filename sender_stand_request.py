import configuration
import requests
import data

def post_new_order(order_body): # функция получения ответа на запрос по созданию заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATING_AN_ORDER,
                          json=data.order_body)

def get_orders_trakt(track): # функция на получение ответа  заказа по треку
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVING_AN_ORDER_BY_NUMBER,
                        params=track)
