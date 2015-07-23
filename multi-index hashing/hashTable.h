#ifndef _HASHTABLE_H_
#define _HASHTABLE_H_
#include "base.h"

class HashTable {
    public:
        HashTable(int);
        ~HashTable();
        void makeTable();

        vector<vector<int> > index;
        int tableId;
};

#endif
