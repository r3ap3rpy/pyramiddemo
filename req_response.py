from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
	url = request.url
	name = request.params.get('name','Not provided!')
	age = request.params.get('age','Not provided!')
	body = f"URL {url} name -> {name} age -> {age} request -> {request}"
	return Response(content_type='text/plain',body=body)

if __name__ == '__main__':
	with Configurator() as config:
		config.add_route("hello","/")
		config.add_view(hello_world,route_name="hello")
		app = config.make_wsgi_app()
	server = make_server('0.0.0.0',6543,app)
	server.serve_forever()
