#include "basic.h"

vector<bitset<SPLITWIDTH> > front_ones, last_ones;
vector<int> variance;

void readData(string fileName) {
    fstream file;
    file.open(fileName.c_str());
    string line;
    while (getline(file, line)) {
        data.push_back(bitset<BITWIDTH>(line));
    }
    return;
}

int hammingDis(bitset<BITWIDTH> a, bitset<BITWIDTH> b) {
    unsigned long t = (a ^ b).to_ulong();
    int counter = 0;
    while (t) {
        counter += (t & 0x01);
        t >>= 1;
    }
    return counter;
}

void calculateVariance() {
    int dataSize = data.size();
    for (int i = 0; i < BITWIDTH; i++) {
        variance.push_back(0);
    }
    for (int i = 0; i < BITWIDTH; i++) {
        for (int j = 0; j < dataSize; j++) {
            if (data[j].test(i)) {
                variance[i]++;
            }
        }
    }
}