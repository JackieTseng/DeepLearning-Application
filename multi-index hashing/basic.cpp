#include "basic.h"

vector<bitset<SPLITWIDTH> > front_ones, last_ones;
vector<int> variance;

// Read binary code from file (csv, sperated by ',')
void readData(string fileName) {
    fstream file;
    file.open(fileName.c_str());
    string line;
    while (getline(file, line)) {
        data.push_back(bitset<BITWIDTH>(line));
    }
    return;
}

// Calculate the variance of each dimension's attribute
// in order to resort the binary code
void calculateVariance() {
    int dataSize = data.size();
    variance = vector<int>(BITWIDTH, 0);
    for (int i = 0; i < BITWIDTH; ++i) {
        for (int j = 0; j < dataSize; ++j) {
            if (data[j].test(i)) {
                ++variance[i];
            }
        }
    }
}
