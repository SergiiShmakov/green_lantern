from flask import Flask
from docker.practice.app.config import Config
from docker.practice.app.models import db, User, Good, Store
from sqlalchemy_utils import create_database, drop_database, database_exists
from docker.practice.app.populate_data import get_users, get_goods, get_stores


def get_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        if database_exists(db.engine.url):
            db.create_all()
            print(f'Database {db.engine.url} exists')
        else:
            print(f'Database {db.engine.url} doesnt exist')
            create_database(db.engine.url)
            db.create_all()
            print(f'Database {db.engine.url} created')

    with app.app_context():
        users = get_users()
        for user in users:
            db.session.add(User(**user))
        db.session.commit()
        print('Database with users successfully recorded')

    with app.app_context():
        goods = get_goods()
        for good in goods:
            db.session.add(Good(**good))
        db.session.commit()
        print('Database with goods successfully recorded')

    with app.app_context():
        stores = get_stores()
        for store in stores:
            db.session.add(Store(**store))
        db.session.commit()
        print('Database with stores successfully recorded')

    return app
