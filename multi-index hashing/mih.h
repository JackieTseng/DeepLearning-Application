#ifndef _MIH_H_
#define _MIH_H_
#include "hashTable.h"

class MIH {
public:
    MIH(int);
    ~MIH();
    void initBinary();
    set<int> searchCandidates(bitset<BITWIDTH>, int);
    set<int> selectGoal(set<int>&, bitset<BITWIDTH>, int);
    vector<bitset<SPLITWIDTH> > split(bitset<BITWIDTH>);
    vector<bitset<SPLITWIDTH> > combine(int);
    int calHammingDis(bitset<BITWIDTH>, bitset<BITWIDTH>);

    int tableNumber;
    vector<HashTable> hashTable; 
};

#endif