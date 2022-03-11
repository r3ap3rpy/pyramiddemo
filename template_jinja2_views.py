from pyramid.view import view_config

@view_config(route_name='home',renderer='hello_world.jinja2')
def home_view(request):
	return dict(name=request.matchdict['name'])

