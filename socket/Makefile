# Makefile for the socket programming example

client_objects = ClientSocket.o Socket.o client.o
server_1_objects = ServerSocket.o Socket.o server_1.o ClientSocket.o
server_2_objects = ServerSocket.o Socket.o server_2.o

all : server_1 server_2 client

server_1: $(server_1_objects)
	g++ -o server_1 $(server_1_objects)

server_2: $(server_2_objects)
	g++ -o server_2 $(server_2_objects)

client: $(client_objects)
	g++ -o client $(client_objects)

Socket: Socket.cpp
ServerSocket: ServerSocket.cpp
ClientSocket: ClientSocket.cpp
client: client.cpp
server_2: server_2.cpp
server_1: server_1.cpp

clean:
	rm -f *.o server_1 server_2 client
