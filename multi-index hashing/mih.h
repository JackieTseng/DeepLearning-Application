#ifndef _MIH_H_
#define _MIH_H_
#include "hashTable.h"

class MIH {
    public:
        MIH(int);
        
        int tableNumber;
        vector<HashTable> hashTable; 
};

#endif
