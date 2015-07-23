#include "mih.h"

int main(int argc, const char *argv[]) {
    string target = "0001100110000000010011111001110111001000011010011011101010001111";
    readData("B.txt");
    MIH x = MIH(4);
    bitset<BITWIDTH> t(target);
    cout << "target : \n";
    cout << t << endl;
    set<int> temp = x.searchCandidates(t, 4);
    cout << "result : \n";
    cout << temp.size() << endl;
    /*
    for (set<int>::iterator it = temp.begin(); it != temp.end(); it++) {
        cout << (*it) << endl;
    }
    */
    cout << "finish\n";
    char a;
    cin >> a;
    return 0;
}