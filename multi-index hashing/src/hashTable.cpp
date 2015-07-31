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
    unsigned long x;
    int single_length = SPLITWIDTH;
    int whole_length = single_length * (HASHTABLENUMBER - 1);
    for (int i = 0; i < length; i++) {
        x = ((data[i] << ((tableId - 1) * (single_length))) >> whole_length).to_ulong();
        index[x].push_back(i);
    }
}