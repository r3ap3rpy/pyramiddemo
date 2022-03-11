from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='home')
def home_view(request):
	return Response("<h1>Welcome home!</h1>")

@view_config(route_name='hello')
def hello_view(request):
	return Response("<h2>Welcome to hello!</h2>")
