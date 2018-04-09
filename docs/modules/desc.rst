Usage
=====
* pip install -r requirements.txt

* ./manage.py 0.0.0.0:9000


Features
========

List hackerspace online hosts
-------------------------------
Server schedules a continuous Nmap scanning in a daemon thread. Each unique host is added to a database. Then we can do `host.online` to determine if host is in the network in the moment. Every host has `.visible` property. It says if the host should be publicly visible or not (is basically means that we can pass `?visible=true` to get them. Only admin user can modify hosts, but anyone can list them.

List hackerspace online guests (users)
--------------------------------------
User have she's assigned hosts under `user.hosts`, if any of theese hosts is `online` and `visible`, then user is `online` to, and you can show them quering `/users?online=true`. To assign host to user. Go to admin panel (/admin), and to Host, then choose user

Open and close intercom doors
-----------------------------
Do a `GET` request to `/intercom` to open an intercom for some amount of time.



Example requests
================

/ - list avaliable urls

/hosts?online=true&visible=true - gets online and visible hosts (only admin can modify hosts)

/users?online=true - list online users

/admin - admin panel for managing users, other db records etc.

/api-auth/login - auth login (Http basic authentication, for now)

/intercom - open intercom (only authernticated users can do this
