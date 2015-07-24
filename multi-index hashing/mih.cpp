#include "mih.h"

MIH::MIH(int _tableNumber) {
    tableNumber = _tableNumber;
    for (int i = 1; i < tableNumber + 1; i++) {
        HashTable* x = new HashTable(i);
        x->makeTable();
        hashTable.push_back(x); 
    }
    initBinary();
}

MIH::~MIH() {
    for (int i = 0; i < tableNumber; i++) {
        delete hashTable[i]; 
    }
}

set<int> MIH::searchCandidates(bitset<BITWIDTH> target, int r) {
    int var = r / tableNumber;
    set<int> result;
    vector<bitset<SPLITWIDTH> > combineBinary;
    for (int i = 0; i <= var; i++) {
        vector<bitset<SPLITWIDTH> > temp = combine(i);
        combineBinary.insert(combineBinary.begin(), temp.begin(), temp.end());
    }
    vector<bitset<SPLITWIDTH> > splitBinary = split(target);
    int maskNumber = combineBinary.size();
    for (int i = 0; i < tableNumber; i++) {
        for (int j = 0; j < maskNumber; j++) {
            unsigned int pos = (splitBinary[i] ^ combineBinary[j]).to_ulong();
            result.insert(hashTable[i]->index[pos].begin(), hashTable[i]->index[pos].end());
        }
    }
    return result;
}

set<int> MIH::selectGoal(set<int>& candidate, bitset<BITWIDTH> target, int r) {
    set<int> result;
    for (set<int>::iterator it = candidate.begin(); it != candidate.end(); it++) {
        bitset<BITWIDTH> temp = data[(*it)];
        int dis = calHammingDis(temp, target);
        if (dis <= r) {
            result.insert(*it);
        }
    }
    return result;
}

void MIH::initBinary() {
    unsigned long t = (unsigned long)pow(2, SPLITWIDTH - 1);
    unsigned long m = (unsigned long)pow(2, SPLITWIDTH) - 1;
    bitset<SPLITWIDTH> x(0);
    int total_len = SPLITWIDTH + 1;
    while (total_len--) {
        front_ones.push_back(x);
        last_ones.push_back(x ^ bitset<SPLITWIDTH>(m));
        x |= t;
        t >>= 1;
    }
}

vector<bitset<SPLITWIDTH> > MIH::combine(int diff_bit) {
    vector<bitset<SPLITWIDTH> > result;
    bitset<SPLITWIDTH> fx = front_ones[diff_bit];
    bitset<SPLITWIDTH> cur_bit = fx;
    int length = cur_bit.size();
    result.push_back(cur_bit);
    if (diff_bit == 0) {
        return result;
    }
    while (true) {
        unsigned long t = (unsigned long)pow(2, SPLITWIDTH - 1);
        int first_one_pos = -1, last_one_pos = -1;
        // Search the first 1's index and last 1's index
        // (Requirement : there is no 0 between these indexes)
        for (int i = 0; i < length; i++) {
            if (first_one_pos == -1) {
                if (cur_bit.to_ulong() & t) {
                    first_one_pos = i;
                }
            } else {
                if (!(cur_bit.to_ulong() & t)) {
                    last_one_pos = i - 1;
                    break;
                }
            }
            t >>= 1;
        }
        if (last_one_pos == -1) {
            break;
        }
        bitset<SPLITWIDTH> first_mask = front_ones[last_one_pos - first_one_pos];
        bitset<SPLITWIDTH> x1 = first_mask | cur_bit;
        bitset<SPLITWIDTH> second_mask = last_ones[last_one_pos] | first_mask;
        bitset<SPLITWIDTH> x2 = second_mask & x1;
        bitset<SPLITWIDTH> third_mask = front_ones[2] >> (last_one_pos);
        cur_bit = third_mask ^ x2;
        result.push_back(cur_bit);
    }
    return result;
}

vector<bitset<SPLITWIDTH> > MIH::split(bitset<BITWIDTH> x) {
    vector<bitset<SPLITWIDTH> > result;
    result.push_back(bitset<SPLITWIDTH>((x >> (BITWIDTH / 4 * 3)).to_ulong()));
    result.push_back(bitset<SPLITWIDTH>(((x << (BITWIDTH / 4)) >> (BITWIDTH / 4 * 3)).to_ulong()));
    result.push_back(bitset<SPLITWIDTH>(((x << (BITWIDTH / 4 * 2)) >> (BITWIDTH / 4 * 3)).to_ulong()));
    result.push_back(bitset<SPLITWIDTH>(((x << (BITWIDTH / 4 * 3)) >> (BITWIDTH / 4 * 3)).to_ulong()));
    return result;
}

int MIH::calHammingDis(bitset<BITWIDTH> a, bitset<BITWIDTH> b) {
    bitset<BITWIDTH> t = (a ^ b);
    int counter = 0;
    while (t != bitset<BITWIDTH>(0)) {
        counter += ((t & bitset<BITWIDTH>(0x01)) != bitset<BITWIDTH>(0));
        t >>= 1;
    }
    return counter;
}