'''
Contains scripts for manipulating docker data/commmands.
'''
import datetime
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
    s.close()

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
    s.close()

    return container

'''
Given time in "yyyy-mm-ddThh:mm:ss.sssssss" format (e.g. 2014-11-15T17:29:09.397073499Z) 
return a datetime object
'''
def convert_time(sTime=""):
    year = int(sTime[:4])
    month = int(sTime[5:7])
    day = int(sTime[8:10])
    hour = int(sTime[11:13])
    minute = int(sTime[14:16])
    second = int(sTime[17:19])    

    return datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)


'''
Starts a docker container(s) with the provided image and options.

Parameters: 
container_name  =   (string) Name of the container
image_name      =   (string) Name of the image to run
quantity        =   (int) Number of containers to run
is_interactive  =   (bool) Specifies whether or not you want terminal access
is_background   =   (bool) Specifies whether the container should run in the background
links           =   (string list) A list of containers to link to
host_mounts     =   (string:string dictionary) A dictionary linking paths to volumes
                    on the host computer to their mount destination in the container
external_mounts =   (string list) A list of containers to mount from
custom_mounts   =   (string list) A list of paths for volumes to create and mount

Returns the response from the last initatied container
'''
def start_container(container_name, image_name, quantity, is_interactive, is_background, 
    links=True, host_mounts=True, external_mounts=True, custom_mounts=True):
    
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

        # Start the container
        response = client.start(container=container.get('Id'), dns=dns_container_ip,
            publish_all_ports=True, volumes_from=external_mounts, links=links_dict, 
            binds=binds_dict)

    # Return the last collected response
    return response


''' 
Resumes a previously stopped docker container

Parameters:
container_name  =   (string) Name of the container

Returns the response from the client start method
'''
def resume_container(container_name):

    # Request a docker client
    client = docker.Client(base_url='unix://var/run/docker.sock', version='1.10', timeout=10)

    # Resume the docker container and return the response
    response = client.start(container=container_name)
    return response


'''
Restarts a running docker container

Parameters:
container_name  =   (string) Name of the container

Returns the response from the client restart method
'''
def restart_container(container_name):

    # Request a docker client
    client = docker.Client(base_url='unix://var/run/docker.sock', version='1.10', timeout=10)

    # Restart the docker container and return the response
    response = client.restart(container=container_name, timeout=10)
    return response


'''
Stops a running docker container

Parameters:
container_name  =   (string) Name of the container

Returns the response from the client stop method
'''
def stop_container(container_name):

    # Request a docker client
    client = docker.Client(base_url='unix://var/run/docker.sock', version='1.10', timeout=10)

    # Stop the docker container and return the response
    response = client.stop(container=container_name, timeout=10)
    return response


'''
Removes a docker container

Parameters:
container_name  =   (string) Name of the container

Returns the response from the client remove method 
'''
def remove_container(container_name):

    # Request a docker client
    client = docker.Client(base_url='unix://var/run/docker.sock', version='1.10', timeout=10)

    # Remove the docker container and return the response
    response = client.remove_container(container=container_name, force=True)
    return response


'''
Unlinks two docker containers

Parameters:
link_name  =   (string) Name of the container link
               It should look something like: linker/base 

Returns the response from the client remove (link) method 
'''
def unlink_containers(link_name):

    # Request a docker client
    client = docker.Client(base_url='unix://var/run/docker.sock', version='1.10', timeout=10)

    # Remove the docker container and return the response
    response = client.remove_container(container=link_name, link=True)
    return response


'''
Removes a docker image

Parameters:
image_name  =   (string) Name of the image

Returns the response from the client remove image method
'''
def remove_image(image_name):

    # Request a docker client
    client = docker.Client(base_url='unix://var/run/docker.sock', version='1.10', timeout=10)

    """ TODO: Call script which removes git repo associated with the image as well """

    # Remove the docker image and return the response
    response = client.remove_image(image=image_name, force=True)
    return response


'''
Branches a docker image

Parameters:
image_name  =   (string) Name of the image we're branching
branch_name =   (string) Name of the new branch

Returns the response from the client commit method
'''
def branch_image(image_name, branch_name):

    # Request a docker client
    client = docker.Client(base_url='unix://var/run/docker.sock', version='1.10', timeout=10)

    # Create a container for the image (so we can use docker commit) and get its ID
    # NOTE: The random number in the container is to reduce the likelihood of accidentally
    # clobbering an existing container. Chosen by fair dice roll - guaranteed randomness
    container = client.create_container(image=image_name, name='temp_container_7432983025')
    containerID = container.get('Id')

    # Create a 'copy' of the image (using docker commit)
    response = client.commit(container=containerID, repository=branch_name, tag="branch")

    """ TODO: Actually call David's copy git repo script """
    # Call bash git copy image repo script

    # Delete the container we made
    client.remove_container(container=containerID, force=True)

    # Return the response from the commit method
    return response