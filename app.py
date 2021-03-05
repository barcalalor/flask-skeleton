import os

from flask import Flask

from api import views
from database import db, migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DB_URL', None)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)

#SET UP DB
db.init_app(app)
migrate.init_app(app, db)

#Register Blueprints
app.register_blueprint(views.camaras)

if __name__ == '__main__':
    app.run(debug=True)
