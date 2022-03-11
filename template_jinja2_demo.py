from wsgiref.simple_server import make_server
from pyramid.config import Configurator

if __name__ == '__main__':
	with Configurator() as config:
		config.add_route('home','/{name}')
		config.include('pyramid_jinja2')
		config.scan('template_jinja2_views')
		app = config.make_wsgi_app()
	server = make_server('0.0.0.0',6543,app)
	server.serve_forever()
