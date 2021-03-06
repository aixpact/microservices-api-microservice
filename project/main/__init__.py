from flask_restplus import Api
from flask import Blueprint

from .controller.user_controller import api as user_ns
from .controller.auth_controller import api as auth_ns

# blueprint = Blueprint('api', __name__)  # original

# Prefix url and move docs to seperate route
# Use versioning
# http://127.0.0.1:5001/api_1/documentation
blueprint = Blueprint('api_1', __name__, url_prefix='/api/v1')

# Add blueprint to Api
api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service',
          doc='/docs/'  # FJE move docs to seperate route
          )

# Add api namespaces like blueprints with url_prefix
api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
