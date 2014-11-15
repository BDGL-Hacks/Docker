'''
Contains scripts for manipulating docker data/commmands.
'''
import json
import re
import StringIO
from subprocess32 import Popen, PIPE

'''
Returns the output of 'docker ps' as a JSON
'''
def get_status():
	# command = "docker ps"
	command = "sudo docker ps"		# Make sure to update so not using sudo

	# Get output from command
	p = Popen(command.split(), stdout=PIPE)
	out, err = p.communicate()

	separator_pattern = re.compile(r"\s\s+")

	# parse output from command and make structure for json
	s = StringIO.StringIO(out)
	headings = separator_pattern.split(s.readline())
	container = { headings[0]: {} }
	for line in s.readlines():
		l = separator_pattern.split(line)
		container[headings[0]][l[0]] = {}
		current = container[headings[0]][l[0]]
		for i in range(1, len(l)):
			current[headings[i]] = l[i]

	json_base = [container]

	return json.dumps(json_base)
