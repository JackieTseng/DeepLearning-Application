#ifndef _BASE_H_
#define _BASE_H_

#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstring>
#include <bitset>
#include <vector>
#include <cmath>
#include <ctime>
#include <set>
using namespace std;

//#define BITWIDTH 1000 // Total binary code's width
//#define HASHTABLENUMBER 50
//#define SPLITWIDTH (BITWIDTH / HASHTABLENUMBER)
//#define RADIUS 4 // The variance for the whole binary code

#define BITWIDTH 64 // Total binary code's width
#define HASHTABLENUMBER 4
#define SPLITWIDTH (BITWIDTH / HASHTABLENUMBER)
#define RADIUS 4 // The variance for the whole binary code

// codes for calculating hamming weight
const unsigned long m1  = 0x5555555555555555; //binary: 0101...  
const unsigned long m2  = 0x3333333333333333; //binary: 00110011..  
const unsigned long m4  = 0x0f0f0f0f0f0f0f0f; //binary: 4 zeros,  4 ones ...  
const unsigned long h01 = 0x0101010101010101; //the sum of 256 to the power of 0,1,2,3...  

struct var {
    float value;
    int number;
    bool operator < (const var& t) const {
        return value < t.value;
    }
};

struct hash_table_number {
    vector<int> number;
    float sum;
    hash_table_number() {
        sum = 0.0;
    }
    bool operator < (const hash_table_number& t) const {
        return sum > t.sum;
    }
};

typedef struct var VAR;
typedef struct hash_table_number HTN;

extern vector<bitset<SPLITWIDTH> > front_ones, last_ones; // codes like 0000.., 1000.., 1100.. and ..0111, ..0011, ..0001
extern vector<bitset<BITWIDTH> > data; // dataset
extern vector<int> hash_number;

void readData(string);
void readDataAndChange(string);
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

// Hamming weight using merge method form wiki
inline int calculateOnes(unsigned long x) {
    x -= (x >> 1) & m1;             //put count of each 2 bits into those 2 bits  
    x = (x & m2) + ((x >> 2) & m2); //put count of each 4 bits into those 4 bits   
    x = (x + (x >> 4)) & m4;        //put count of each 8 bits into those 8 bits   
    return (x * h01) >> 56;
}

inline unsigned long ulong_swap(unsigned long v, int x, int y) {
    x = SPLITWIDTH - x - 1;
    y = SPLITWIDTH - y - 1;
    return v & (~(1 << x)) & (~(1 << y)) | (((v >> y) & 1) << x) | (((v >> x) & 1) << y);
}

inline bitset<BITWIDTH>& bit_swap(bitset<BITWIDTH>& v, int x, int y) {
    x = BITWIDTH - x - 1;
    y = BITWIDTH - y - 1;
    v = v & ((~(bitset<BITWIDTH>(1) << x)) & ~(bitset<BITWIDTH>(1) << y)) | (((v >> y) & bitset<BITWIDTH>(1)) << x) | (((v >> x) & bitset<BITWIDTH>(1)) << y);
    return v;
}

inline bitset<BITWIDTH>& bit_transform(bitset<BITWIDTH>& v) {
    for (int i = 0; i < BITWIDTH; i++) {
        bit_swap(v, i, hash_number[i]);
    }
    return v;
}

inline bitset<BITWIDTH> add(bitset<BITWIDTH> a, bitset<BITWIDTH> b) {
    bitset<BITWIDTH> carry, add;
    do {
        add = a ^ b;
        carry = (a & b) << 1;
        a = add;
        b = carry;
    } while (carry != 0);
    return add;
}

inline bitset<BITWIDTH> subtract(bitset<BITWIDTH> a, bitset<BITWIDTH> b) {
    return add(a, add(~b, bitset<BITWIDTH>(1)));
}

inline int calculateOnes_2(bitset<BITWIDTH> number) {
    int count_ = 0;
    bitset<BITWIDTH> one = bitset<BITWIDTH>(1);
    while (number != 0) {
        number &= subtract(number, one);
        count_ ++;
    }
    return count_;
}
#endif
