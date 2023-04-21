"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch13ckrh4hstbhh94br0-a.oregon-postgres.render.com",
        database="todo_jkbn",
        user="todo_jkbn_user",
        password="aob3YKq1oX3Yt5MXALRBzb3rxPwH550r")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
