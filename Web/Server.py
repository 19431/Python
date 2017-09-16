# A web server that handle GET requests from multiple clients concurrently using TCP/IP connection #

import os
import errno
import signal
import socket

queue_size = 1024


# gets called to process client request "needs more work in order to deal with other request other than get"
def process_a_request(client_connection):
    new_request = client_connection.recv(queue_size)
    print(new_request.decode())

    # gives GET response in typical HTTP format
    new_response = b"""\HTTP/1.1 200 OK"""
    client_connection.sendall(new_response)


# Reaps zombie processes resulting from forking
def reap_zombie(signum, frame):
    while True:
        try:

            # Wait for all child processes to be done
            pid, status = os.waitpid(-1, os.WNOHANG)
        except OSError:
            return

        # stop reaping when all zombies are gone
        if pid == 0:
            return


# create a socket and bind it to an address
def serve():
    # set the server address
    server_address = '', 8888

    # bind socket to address
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(queue_size)
    print("starting up %s on port %s " % server_socket.getsockname())

    signal.signal(signal.SIGCHLD, reap_zombie)

    while True:
        try:
            connection, client_addr = server_socket.accept()
        except IOError as IO_error:
            if IO_error.errno == errno.EINTR:
                continue
            else:
                raise

        pid = os.fork()

        if pid != 0:  # it is the parent
            # parent should not run before child, loop again
            connection.close()

        else:  # it is the child
            server_socket.close()  # no need to keep open, child not accepting any new clients
            process_a_request(connection)

            # close connection after client's request has been processed
            os.exit(0)


if __name__ == '__main__':
    serve()
