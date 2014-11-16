'''
Given docker container id, print its ip address
'''
import sys
from docker.manager import utils

def get_ip(container_id=""):
	info = utils.get_info(container_id)[0]
	print info["NetworkSettings"]["IPAddress"]

if __name__=="__main__":
	get_ip(sys.argv[1])