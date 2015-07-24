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