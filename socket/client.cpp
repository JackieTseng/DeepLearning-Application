#include "ClientSocket.h"
#include "SocketException.h"
#include <iostream>
#include <string>
using namespace std;

const string kServer_Address = "172.22.192.45";

int main(int argc, char* argv[]){
    try {
        ClientSocket client_socket(kServer_Address, 30000);
        std::string reply;
        while (1) {
            try {
                std::cin >> reply;
                client_socket << reply;
                client_socket >> reply;
            } catch(SocketException&){}
            std::cout << "We received this response from the server:\n\"" << reply << "\"\n";;
        }
    } catch(SocketException& e) {
        std::cout << "Exception was caught:" << e.description() << "\n";
    }
    return 0;
}
