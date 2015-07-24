#include "hashTable.h"

vector<bitset<BITWIDTH> > data;

HashTable::HashTable(int _tableId) {
    int length = (int)pow(2, SPLITWIDTH) - 1;
    index = vector<vector<int> >(length, vector<int>());
    tableId = _tableId;
}

HashTable::~HashTable() {
}

void HashTable::makeTable() {
    int length = data.size();
    for (int i = 0; i < length; i++) {
        bitset<BITWIDTH> cur = data[i];
        unsigned int x;
        switch(tableId) {
            case 1:
                x = (cur >> 48).to_ulong();
                break;
            case 2:
                x = ((cur << 16) >> 48).to_ulong();
                break;
            case 3:
                x = ((cur << 32) >> 48).to_ulong();
                break;
            case 4:
                x = ((cur << 48) >> 48).to_ulong();
                break;
        }
        index[x].push_back(i);
    }
}