#include "ServerSocket.h"
#include "SocketException.h"
#include "ClientSocket.h"
#include <iostream>
#include <string>

const std::string kServer_Address = "172.22.192.45";

int main(int argc, char* argv[]) {
    std::cout << "Server 1 running....\n";
    try {
        ServerSocket server(30000);
        while(true) {
            ServerSocket new_sock;
            server.accept(new_sock);
            try {
                while(true) {
                    std::string data;
                    new_sock >> data;
                    std::cout << "Server 1 receive " + data << std::endl;
                    ClientSocket client_socket(kServer_Address, 30001);
                    client_socket << ("Good morning, " + data);
                    client_socket >> data;
                    new_sock << data;
                }
            } catch(SocketException&){}
        }
    } catch(SocketException& e) {
        std::cout << "Exception was caught:" << e.description() << "\nExiting.\n";
    }
    return 0;
}
