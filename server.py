# file imports
import socket
import requests
import validators


# global variables
HOST = "127.0.0.1" # IP address that server is running on
MAXLINE = 1024
port = -1

# set port to input, make sure that it is a number
while port == -1:
    try:
        port = int( input( "Enter a port number: " ) ) # port number that the server is listening on
    except ValueError:
        print( "Port entered is not a number, try again" )
        port = -1

def handleRequest( request ):
    # if request is exit, return exit
    if request.decode() == "exit":
        return "exit".encode()

    # make sure url is valid
    if not validators.url( request.decode() ):
        return "Not a valid URL, try again".encode()

    # get request and check if request exists
    try:
        r = requests.get( request, auth = ( 'user', 'pass' ) )
    except requests.exceptions.ConnectionError:
        return "URL does not exitst, try again".encode()

    # return request info
    return "Handling Request...\n--------Request:\t{}\n--------Status Code:\t{}\n--------Headers:\t{}\n--------Encoding:\t{}".format( request.decode(), r.status_code, r.headers['content-type'], r.encoding ).encode()


# create a server socket
with socket.socket( socket.AF_INET, socket.SOCK_STREAM ) as sock:
    # bind the server socket to the port and IP address
    sock.bind( ( HOST, port ) )

    # listen for incoming client connections
    sock.listen()

    # accept client connection
    connection, address = sock.accept()
    with connection:
        # display connection successful
        print( "Connected to client at ", address )

        # send welcome message
        connection.sendall( "Welcome to UrlInformer!\nPlease enter a complete URL to recieve the basic info about it.\nEnter 'exit' to exit!".encode() )

        # loop continuously
        while True:
            # recieve data
            request = connection.recv( MAXLINE )

            # handle data
            response = handleRequest( request )

            # send data
            connection.sendall( response )

            # if exit, break the loop
            if request.decode() == "exit":
               break

    # close the connection and socket
    connection.close()
    sock.close()

# close python script
quit()