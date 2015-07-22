#include <iostream>
#include <fstream>
#include <cstring>
#include <bitset>
#include <vector>
using namespace std;
#define BITWIDTH 64

vector<bitset<BITWIDTH> > data;

int main(int argc, const char *argv[]) {
    fstream file;
    file.open("B.txt");

    string line;
    while (getline(file, line)) {
        data.push_back(bitset<64>(line));
    }
    cout << data.size();
    return 0;
}
