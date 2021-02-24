from chalice import Blueprint

extra_routes = Blueprint(__name__)

@extra_routes.route('/foo')
def foo():
  return {'foo': 'bar'}