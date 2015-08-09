#ifndef _MIH_H_
#define _MIH_H_
#include "hashTable.h"

class MIH {
    public:
        MIH(const int&);
        ~MIH();

        // Initialize the fixed-length 0-1's binary codes
        void initBinary();
        // Search the candidates from the hashtables by matching indexes
        set<int>& searchCandidates(const bitset<BITWIDTH>&, const int&, set<int>&);
        // Select the final result from the candidates set by hamming weight
        set<int>& selectGoal(const set<int>&, const bitset<BITWIDTH>&, const int&, set<int>&);
        // Generate the combine codes for a given code
        vector<bitset<SPLITWIDTH> >& combine(const int&, vector<bitset<SPLITWIDTH> >&);
        // Calculate hamming weight between two codes
        int calHammingDis(const bitset<BITWIDTH>&, const bitset<BITWIDTH>&, const int&);

    private:
        int tableNumber;
        vector<HashTable*> hashTable; 
};

#endif
