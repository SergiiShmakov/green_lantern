import csv


def get_users():
    with open('../data/users.csv', 'r') as f:
        reader = csv.DictReader(f)
        users = [i for i in reader]
    return users


def get_goods():
    with open('../data/goods.csv', 'r') as f:
        reader = csv.DictReader(f)
        goods = [i for i in reader]
    return goods


def get_stores():
    with open('../data/stores.csv', 'r') as f:
        reader = csv.DictReader(f)
        stores = [i for i in reader]
    return stores
