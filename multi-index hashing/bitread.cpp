#include <iostream>
#include <fstream>
#include <cstring>
#include <bitset>
#include <vector>
using namespace std;
#define BITWIDTH 64

vector<bitset<BITWIDTH> > data;

void readData(string);
int hammingDis(bitset<BITWIDTH>, bitset<BITWIDTH>);

int main(int argc, const char *argv[]) {
    readData("B.txt");
    return 0;
}

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
