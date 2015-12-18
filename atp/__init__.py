from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.restless import APIManager
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from webassets import Environment, Bundle

app = Flask(__name__)
app.config.from_object('atp.config.DevelopmentConfig')

assets = Environment(app)

foundation_js = Bundle(
    'atp/static/bower_components/fastclick/lib/fastclick.js',
    'atp/static/bower_components/viewport-units-buggyfill/viewport-units-buggyfill.js',
    'atp/static/bower_components/tether/tether.js',
    'atp/static/bower_components/hammerjs/hammer.js',
    'atp/static/bower_components/angular/angular.js',
    'atp/static/bower_components/angular-animate/angular-animate.js',
    'atp/static/bower_components/angular-ui-router/release/angular-ui-router.js',
    'atp/static/bower_components/foundation-apps/js/vendor/iconic.min.js',
    'atp/static/bower_components/foundation-apps/js/angular/foundation.js',
    filters='jsmin', output='assets/foundation.js')
assets.register('foundation_js', foundation_js)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
api_manager = APIManager(app, flask_sqlalchemy_db=db)

from atp import views, models, api
