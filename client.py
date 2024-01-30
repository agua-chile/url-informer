# file imports
import socket
import sys

# global variables
HOST = "127.0.0.1"  # the server's hostname or IP address
MAXLINE = 1024
port = -1

# set port to input, make sure that it is a number
while port == -1:
    try:
        port = int( input( "Enter a port number: " ) ) # the port used by the server
    except ValueError:
        print( "Port entered is not a number, try again" )
        port = -1

# create a server socket
with socket.socket( socket.AF_INET, socket.SOCK_STREAM ) as sock:
    # connect to server
    try:
        sock.connect( ( HOST, port ) )
        print( "--------Connecting to Server--------" )
    # if error, display and quit
    except:
            print( "Error: ", sys.exc_info()[0], " occured, script closing" )
            quit()

    data = sock.recv( MAXLINE )
    print( data.decode() )

    # loop continuously
    while True:
        # send data to server
        sock.sendall( bytes( input( ">>Client: " ), "utf-8" ) )

        # recieve data
        response = sock.recv( MAXLINE )

        # if exit, break the loop
        if response.decode() == "exit":
            break

        # display recieved data
        print( ">>Server:", response.decode() )

    # close the socket
    sock.close()

# display exit
print( "--------Closing connection with Server--------" )

# close python script
quit()