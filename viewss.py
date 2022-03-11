from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='home')
def home_view(request):
	body = "first: %(first)s second: %(second)s" % request.matchdict
	return Response(body)

