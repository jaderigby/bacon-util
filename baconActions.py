import sys, create, addBacon

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None

if action == None:
	create.execute()

elif action == 'add':
	origin = str(sys.argv[0].replace('/bacon-util/baconActions.py', ''))
	addBacon.execute(origin)
