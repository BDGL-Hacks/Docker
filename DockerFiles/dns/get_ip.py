'''
Given docker container id, print its ip address
'''
import sys
import time
from docker.manager import utils

def get_ip(container_id=""):
	while True:
		try:
			info = utils.get_info(container_id)[0]
		except:
			time.sleep(1)
			continue
		break

	print info["NetworkSettings"]["IPAddress"]

if __name__=="__main__":
	get_ip(sys.argv[1])
