#ifndef _BASE_H_
#define _BASE_H_

#include <iostream>
#include <fstream>
#include <cstring>
#include <bitset>
#include <vector>
#include <cmath>
#include <ctime>
#include <set>
using namespace std;

#define BITWIDTH 64
#define HASHTABLENUMBER 4
#define SPLITWIDTH (BITWIDTH / HASHTABLENUMBER)
#define RADIUS 4

extern vector<bitset<SPLITWIDTH> > front_ones, last_ones;
extern vector<bitset<BITWIDTH> > data;
extern vector<int> variance;

void readData(string);
void calculateVariance();
inline vector<bitset<SPLITWIDTH> >& split(bitset<BITWIDTH> B, vector<bitset<SPLITWIDTH> >& result) {
    unsigned long temp;
    int single_length = SPLITWIDTH;
    int whole_length = single_length * (HASHTABLENUMBER - 1);
    for (int i = 0; i < HASHTABLENUMBER; ++i) {
        temp = ((B << (i * single_length)) >> whole_length).to_ulong();
        result.push_back(bitset<SPLITWIDTH>(temp));
    }
    return result;
}
#endif