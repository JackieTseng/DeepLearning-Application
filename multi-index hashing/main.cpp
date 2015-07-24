#include "mih.h"

int main(int argc, const char *argv[]) {
    double _1_, _2_, _3_, _4_;
    string target = "0001100110000000010011111001110111001000011010011011101010001111";
    _1_ = clock();
    readData("B.txt");
    MIH x = MIH(4);
    _2_ = clock();
    bitset<BITWIDTH> t(target);
    set<int> temp = x.searchCandidates(t, 4);
    _3_ = clock();
    set<int> result = x.selectGoal(temp, t, 4);
    _4_ = clock();
    cout << "result : " << result.size() << endl;
    cout << "Bulid time           : " << _2_ - _1_ << endl;
    cout << "Find Candidate  time : " << _3_ - _2_ << endl;
    cout << "Find Goal time       : " << _4_ - _3_ << endl;
    cout << "Total time           : " << _4_ - _1_ << endl;
    /*
    for (set<int>::iterator it = temp.begin(); it != temp.end(); it++) {
        cout << (*it) << endl;
    }
    */
    cout << "finish\n";
    char a;
    a = getchar();
    return 0;
}