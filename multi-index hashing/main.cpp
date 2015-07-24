#include "mih.h"

int main(int argc, const char *argv[]) {
    double _1_, _2_, _3_, _4_;
    string target = "0011101110000010010011111001111110001110001010001110100010001011";
    //string target = "0010100001011001101001000001100110000111010011101000001100010111";
    _1_ = clock();
    readData("B.txt");
    MIH x = MIH(HASHTABLENUMBER);
    _2_ = clock();
    bitset<BITWIDTH> t(target);
    set<int> temp = x.searchCandidates(t, RADIUS);
    _3_ = clock();
    set<int> result = x.selectGoal(temp, t, RADIUS);
    _4_ = clock();
    cout << "result : " << result.size() << endl;
    cout << "Bulid time           : " << _2_ - _1_ << endl;
    cout << "Find Candidate  time : " << _3_ - _2_ << endl;
    cout << "Find Goal time       : " << _4_ - _3_ << endl;
    cout << "Total time           : " << _4_ - _1_ << endl;
    cout << "finish\n";
    char a = getchar();
    return 0;
}