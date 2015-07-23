#ifndef _BASE_H_
#define _BASE_H_

#include <iostream>
#include <fstream>
#include <cstring>
#include <bitset>
#include <vector>
#include <cmath>
using namespace std;

#define BITWIDTH 64
#define SPLITWIDTH 16

extern vector<bitset<SPLITWIDTH> > front_ones, last_ones;
extern vector<bitset<BITWIDTH> > data;
extern vector<int> variance;

void readData(string);
void calculateVariance();
void initBinary();
void combine(int);
int hammingDis(bitset<BITWIDTH>, bitset<BITWIDTH>);

#endif
