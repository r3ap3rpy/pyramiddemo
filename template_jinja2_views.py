from pyramid.view import view_config

@view_config(route_name='hello',renderer='hello_world.jinja2')
def hello_view(request):
	return dict(name=request.matchdict['name'])

@view_config(route_name='hello_json', renderer = 'json')
def hello_json(request):
	return [1,'a',1.1]

@view_config(route_name='my_class')
class HellClass:
	def __init__(self,request):
		self.name = request.matchdict['name']

	@view_config(renderer='hello.jinja2')
	def hello_view(self):
		print("Simply view")
		return dict()
