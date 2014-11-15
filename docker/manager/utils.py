'''
Contains scripts for manipulating docker data/commmands.
'''
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
	counter = 1
	container = {}
	for line in s.readlines():
		container[counter] = {}
		l = separator_pattern.split(line)
		for i in range(len(l)):
			container[counter][headings[i]] = l[i]

		counter += 1

	return container