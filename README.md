## URL Informer

### Intro

Hello and welcome to my Web Assignment 1 for CS 460. This is a simple client-server
program that takes a URL from the client, sends it to the server, and then the server 
sends back the URL along with the status code, URL headers, and the URL encoding.

### Compiling

To run this program you need to have Python3 installed along with the Python packages:
    socket
    requests
    validators
    sys

These can be installed with a simple `pip install` but validators must be installed with `pip3 install`

The files needed are `server.py` and `client.py`.

### Instructions

With terminal window 1, run the command: `python3 server.py`
With terminal window 2, run the command: `python3 client.py`

When running each, you will be prompted to enter a port number; make sure they are the same
You will then see an some brief instructions with an input prompt

If you get this error when trying to run either of the files:

Traceback (most recent call last):
  File `server.py`, line 34, in <module>
    sock.bind( ( HOST, PORT ) )
OSError: [Errno 48] Address already in use

Change the port number on both server.py and client.py and try again

How this works:

The client connects to the server and sends over the request of a website URL
The server then takes the request, makes sure that it is valid and real
Then the server sends back the URL along with the status code, URL headers, and the URL encoding