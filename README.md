## HACKERSPACE

#ABOUT

It's a hackerspace command centre. Made for [hackerspace-lbn link](www.hackerspace-lbn.pl), but it's configurable and make with other places in mind.


#FEATURES

Hosts
=====
Lists hackerspace online guests
-------------------------------
Server schedules a continuous Nmap scanning in a daemon thread. Each unique host is added to a database. Then we can do `host.online` to determine if host is in the network in the moment. Every host has `.visible` property. It says if the host should be publicly visible or not (is basically means that we can pass `?visible=true` to get them. Only admin user can modify hosts, but anyone can list them.

Intercom
========
Open and close intercom doors
-----------------------------
Do a `GET` request to `/intercom` to open an intercom for some amount of time.


EXAMPLE REQUESTS
================
/ - list avaliable urls

/hosts?online=true&visible=true - gets online and visible hosts (only admin can modify hosts)

/admin - admin panel for managing users, other db records etc.

/api-auth/login - auth login (Http basic authentication, for now)

/intercom - open intercom (only authernticated users can do this
