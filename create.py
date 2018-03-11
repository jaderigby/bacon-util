#===================================================================
#
#	HEADER
#
import sys, re, subprocess

from scab import scab as s

#===================================================================

def execute():

	origin = '/Users/jaderigby/Documents/'

	t = s.scab()
	t.scan('{}bash-tools/bacon-util/template'.format(origin))
	# t.reIgnore('(/\.+)|(create\.py)')
	t.record()
	name = raw_input("Give your tool a name: ")
	t.build('{}/bash-tools/{}'.format(origin, name))
	alias = raw_input("What would you like the alias to be? ")

	def write_to_bashrc(FILEPATH, ALIAS, EXECUTE):
		FILE = open(FILEPATH, 'r')
		data = FILE.read()
		FILE.close()
		data = data + '\nalias ' + ALIAS + '=' + EXECUTE
		FILE = open(FILEPATH, 'w')
		FILE.write(data)
		FILE.close()

	def replace_generic_reference_with_actual(FILEPATH, NAME, PLACEHOLDER):
		FILE = open(FILEPATH, 'r')
		data = FILE.read()
		FILE.close()
		data = data.replace(PLACEHOLDER, NAME)
		FILE = open(FILEPATH, 'w')
		FILE.write(data)
		FILE.close()

	executionString = '"python {}bash-tools/{}/actions.py"'.format(origin, name)

	write_to_bashrc('{}bash-tools/.bashrc'.format(origin), alias, executionString)

	replace_generic_reference_with_actual(origin + 'bash-tools/'+ name +'/settings.py', name, '<tool-name>')
	replace_generic_reference_with_actual(origin + 'bash-tools/'+ name +'/messages.py', name, '<tool-name>')
	# replace_generic_reference_with_actual(origin + 'bash-tools/'+ name +'/messages.py', name, '<tool-name>')

	print('''
[ Process Complete ]
	''')

# subprocess.call(['source', '~/Documents/bash-tools/.bashrc'], shell=True)
#
# subprocess.call(['source', '~/.bash_profile'], shell=True)
