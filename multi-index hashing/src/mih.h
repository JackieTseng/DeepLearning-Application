#ifndef _MIH_H_
#define _MIH_H_
#include "hashTable.h"

class MIH {
    public:
        MIH(const int&);
        ~MIH();
        void initBinary();
        set<int>& searchCandidates(const bitset<BITWIDTH>&, const int&, set<int>&);
        set<int>& selectGoal(const set<int>&, const bitset<BITWIDTH>&, const int&, set<int>&);
        vector<bitset<SPLITWIDTH> >& combine(const int&, vector<bitset<SPLITWIDTH> >&);
        int calHammingDis(const bitset<BITWIDTH>&, const bitset<BITWIDTH>&, const int&);

    private:
        int tableNumber;
        vector<HashTable*> hashTable; 
};

#endif
