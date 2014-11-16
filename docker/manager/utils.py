'''
Contains scripts for manipulating docker data/commmands.
'''
import docker
import json
import re
import StringIO
from subprocess32 import Popen, PIPE

'''
Return the output of 'docker ps' as a json

TODO: Update so command does not use sudo
'''
def get_status():
    # command = "docker ps -a"
    command = "sudo docker ps -a"

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

'''
Return json containing container-specific docker information for given container id

TODO: Update so command does not use sudo
'''
def get_info(container_id=""):
    # command = "docker inspect " + container_id
    command = "sudo docker inspect " + container_id 

    # Get output from command
    p = Popen(command.split(), stdout=PIPE)
    out, err = p.communicate()

    # Convert to json and return
    s = StringIO.StringIO(out)
    return json.load(s)

'''
Return the output of 'docker images' as a json

TODO: Update so command does not use sudo
'''
def get_images():
    # command = "docker images"
    command = "sudo docker images"
    
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

        # Don't include empty/temporary images in return value
        if "<none>" not in l[0]:
            for i in range(len(l)):
                container[counter][headings[i]] = l[i]

            counter += 1

    return container

'''
Starts a docker container with the provided image and options.

Parameters: 
container_name  =   (string) Name of the container
image_name      =   (string) Name of the image to run
quantity        =   (int) The number of containers to create
links           =   (string list) A list of containers to link to
host_mounts     =   (string:string dictionary) A dictionary linking paths to volumes
                    on the host computer to their mount destination in the container
external_mounts =   (string list) A list of containers to mount from
custom_mounts   =   (string list) A list of paths for volumes to create and mount
is_interactive  =   (bool) Specifies whether or not you want terminal access
is_background   =   (bool) Specifies whether the container should run in the background

Returns the response from the client start method
'''
def start_container(container_name, image_name, quantity, links, host_mounts,
    external_mounts, custom_mounts, is_interactive, is_background):
    
    # Request a docker client
    client = docker.Client(base_url='unix://var/run/docker.sock', version='1.10', timeout=10)

    # Create a list of all volume paths to mount (not incuding those from other containers)
    all_volumes = host_mounts.values() + custom_mounts

    # Convert the links argument into a dictionary
    links_dict = {}
    for link in links:
        links_dict[link] = link

    # Create the volume mount binds dictionary
    binds_dict = {}
    for host_path in host_mounts:
        dest_path = host_mounts[host_path]
        binds_dict[host_path] = {'bind' : dest_path, 'ro' : False}

    # Get DNS container IP address
    dns_container_inspect_dict = client.inspect_container("base")
    dns_container_NetworkSettings_dict = dns_container_inspect_dict["NetworkSettings"]
    dns_container_ip = [dns_container_NetworkSettings_dict["IPAddress"]]

    # Create (quantity) number of containers
    for i in range(quantity):

        # Ensure each container has a unique name
        unique_name = container_name
        if (i != 0):
            unique_name += str(i+1)

        # Create a container and get its id
        container = client.create_container(image=image_name, name=unique_name, 
            volumes=all_volumes, tty=is_interactive, stdin_open=is_interactive, 
            detach=is_background)
        containerID = container.get('Id')

        # Start the container and return the response
        response = client.start(container=container.get('Id'), dns=dns_container_ip,
            publish_all_ports=True, volumes_from=external_mounts, links=links_dict, 
            binds=binds_dict)
    return response
