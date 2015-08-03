// Definition of the ServerSocket class
#ifndef SERVER_SOCKET_H
#define SERVER_SOCKET_H

#include "Socket.h"

class ServerSocket : private Socket {
    public:
        ServerSocket(int port);
        ServerSocket () {};
        virtual ~ServerSocket();
        const ServerSocket& operator <<(const std::string&)const;
        const ServerSocket& operator >>(std::string&)const;
        void accept(ServerSocket&);
};

#endif
