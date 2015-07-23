#include <iostream>
#include <fstream>
#include <cstring>
#include <bitset>
#include <vector>
#include <cmath>
using namespace std;
#define BITWIDTH 64
#define SPLITWIDTH 16

vector<bitset<SPLITWIDTH> > front_ones, last_ones;
vector<bitset<BITWIDTH> > data;
vector<int> variance(BITWIDTH);

void readData(string);
void calculateVariance();
int hammingDis(bitset<BITWIDTH>, bitset<BITWIDTH>);
void initBinary();
void combine(int);

int main(int argc, const char *argv[]) {
    //readData("B.txt");
    //calculateVariance();
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

void calculateVariance() {
    int dataSize = data.size();
    for (int i = 0; i < BITWIDTH; i++) {
        for (int j = 0; j < dataSize; j++) {
            if (data[j].test(i)) {
                variance[i]++;
            }
        }
    }
}

void initBinary() {
    unsigned long t = pow(2, SPLITWIDTH - 1);
    unsigned long m = pow(2, SPLITWIDTH) - 1;
    bitset<SPLITWIDTH> x(0);
    int total_len = SPLITWIDTH + 1;
    while (total_len--) {
        front_ones.push_back(x);
        last_ones.push_back(x ^ bitset<SPLITWIDTH>(m));
        x |= t;
        t >>= 1;
    }
}

void combine(int diff_bit) {
    initBinary();    
    vector<bitset<SPLITWIDTH> > result;
    bitset<SPLITWIDTH> fx = front_ones[diff_bit];
    bitset<SPLITWIDTH> cur_bit = fx;
    //bitset<SPLITWIDTH> cur_bit(string("01110100"));
    int length = cur_bit.size();
    result.push_back(cur_bit);
    while (true) {
        unsigned long t = pow(2, SPLITWIDTH - 1);
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
                if (i == length - 1) {
                    last_one_pos = i;
                }
            }
            t >>= 1;
        }
        if (last_one_pos ==  length - 1) {
            break;
        }
        //cout << first_one_pos << " " << last_one_pos << endl;
        bitset<SPLITWIDTH> first_mask = front_ones[last_one_pos - first_one_pos];
        bitset<SPLITWIDTH> x1 = first_mask | cur_bit;
        bitset<SPLITWIDTH> second_mask = last_ones[last_one_pos] | first_mask;
        bitset<SPLITWIDTH> x2 = second_mask & x1;
        bitset<SPLITWIDTH> third_mask = front_ones[2] >> (last_one_pos);
        cur_bit = third_mask ^ x2;
        result.push_back(cur_bit);
    }
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << endl;
    } 
}
