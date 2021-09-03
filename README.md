# Blasteroids

Blasteroids is a multi-player space shooter written in Python as a proof-of-concept for future projects.

# Playing

You'll need a server running, and best to do it in a Python virtual environment. Do something like this:

    $> python3 -m venv env
    $> source env/bin/activate
    $> pip install -r requirements.txt
    $> bin/run_server.sh

Then you'll want to connect a client so you can shoot things. Do something like this:

    $> bin/run_client.sh

## Controls

Use the left and right arrow keys to rotate, the up arrow key to accelerate forward, and the spacebar to shoot. That's it.

# Authors

* Cameron Hale (Small Army Summer Intern)
* Jamie Hale (Cameron's Dad)
