from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from datetime import datetime
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

app = Flask(__name__)



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///don_records.db'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)

    # Register the format_datetime filter
    @app.template_filter('format_datetime')
    def format_datetime(value):
        if value is None:
            return ""
        return value.strftime('%B %d, %Y %H:%M')

    @app.template_filter('format_currency')
    def format_currency(value):
        return "Ksh {:,.2f}".format(value)

    from app.routes import main
    app.register_blueprint(main.bp)

    from app.routes import auth
    app.register_blueprint(auth.bp)

    from app.routes import admin
    app.register_blueprint(admin.bp)

    from app.routes import artist
    app.register_blueprint(artist.bp)

    from app.routes import producer
    app.register_blueprint(producer.bp)

    from app.routes import blog
    app.register_blueprint(blog.bp)

    from app.routes import payment
    app.register_blueprint(payment.bp)
  

    return app