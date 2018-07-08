from flask import Flask, send_file, abort
from flask_bcrypt import Bcrypt
from BusTrack.repository.main import create_database
import sqlite3

app = Flask(__name__, instance_relative_config=True)
conn = sqlite3.connect('data_1.db', check_same_thread=False)
conn.isolation_level = None
db = conn.cursor()
bcrypt = Bcrypt(app)

from BusTrack.views.admin import admin
from BusTrack.views.driver import driver
from BusTrack.views.parent import parent

# add admin blueprint
app.register_blueprint(admin, url_prefix='/admin')
# add parent blueprint
app.register_blueprint(parent, url_prefix='/api/v1/parent')
# add driver blueprint
app.register_blueprint(driver, url_prefix='/api/v1/driver')

create_database()
