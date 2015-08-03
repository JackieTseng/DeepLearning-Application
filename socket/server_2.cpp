#include "ServerSocket.h"
#include "SocketException.h"
#include <iostream>
#include <string>

int main(int argc, char* argv[]) {
    std::cout << "Server 2 running....\n";
    try {
        ServerSocket server(30001);
        while(true) {
            ServerSocket new_sock;
            server.accept(new_sock);
            try {
                while(true) {
                    std::string data;
                    new_sock >> data;
                    std::cout << "Server 2 receive " + data << std::endl;
                    new_sock << ("Good afternoon, " + data);
                }
            } catch(SocketException&){}
        }
    } catch(SocketException& e) {
        std::cout << "Exception was caught:" << e.description() << "\nExiting.\n";
    }
    return 0;
}
