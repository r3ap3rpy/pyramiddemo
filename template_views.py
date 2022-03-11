from pyramid.view import view_config

@view_config(route_name='home',renderer='hello_world.pt')
def home_view(request):
	return dict(name=request.matchdict['name'])

