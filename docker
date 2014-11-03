Docker

We are trying to provide a cloud environment to those that only have a single computer. This program should allow one computer to create multiple docker
instances each with their own ip address and services.

Features

  *Every docker instance "represents" a different machine. As such they should all have unique ip addresses
    **This might have to be done by running each docker instance inside of the first docker instance.
        **This would allow the first instance to assign ip addresses for subsequent instances 
        **In order to access the "private network" given by the first docker instance we may need to use an http proxy
            ***This proxy also allows other people on the same private network to use those exact docker instances
  *There should be an easy way to give web servers their own URLs.
    **This can be accomplished with one of the docker instances acting as a DNS server
    ***Bonus to this approach is that the DNS nameserver is consistent and can be updated easily, don't need to purchase domain names for testing.


Requirements for our docker image

    *Http proxy, DNS server, ability to create more docker instances
    *Web server to allow a GUI for options such as pre-created docker, image tracking
    *Version control?

Private website in first docker image

    *Image tracking
        *Name of images
        *IP address of images
        *traffic of images
        *allows one to ssh into images?
    *GUI for common docker commands?
    *Easy to set up images
        *LAMP/LEMP
        *MongoDB
        *MySQL/PHPmyAdmin
        *Django
        ^Wordpress
    *Ability to "send images" to other IP addresses?
        *How are we going to allow for set-up on different devices once everything has been created?
            *Ideally we should start everything on the one computer and let you "push" images out to other servers that you own
Public Web App
    *Who are we
    *Public image uploading/downloading
    *Download the original docker image
    *Image tracking for public images (I personally think this belongs to the "first docker image" always)  

Why this is helpful
    *Unique IP addresses allows you to better replicate real life environment
        *Deal with routing issues
        *Deal with High Availability issues
        *Deal with firewall issues

TODO list
    *Set up isolation environment
        *Allow for unique IP addresses
        *Allow for HTTP proxy
        *Allow for DNS server
        *Connect from the private network
    *Private web app
        *Easy set-up images
        *Access to a command line for creating new dockers
        *ability to ssh into other dockers?
        *GUI for basic docker commands
    *Bells and Whistles
        *Ability to send out docker images (impressive but prob hard)
        *Public facing website (basic purpose is to direct people to the git repo and boot2docker)
        *Cool Graphs for docker connectivity
        *High Availability Testing
            *Specifically databases (Master/Slave)
