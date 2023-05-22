#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

long double recursion(int n){
    long double res;
    if (n==1){
        return exp(-1);
    }
    else{
    res=1-(n*recursion(n-1));
    return res;
    }
}

int main(){
    long double res;
    int n=10;
    res=recursion(n);
    cout.precision(10);
    cout<<"n="<<n<<"\tSingle precision="<<float(res)<<"\tDouble precision="<<res<<"\n";
    n=15;
    res=recursion(n);
    cout<<"n="<<n<<"\tSingle precision="<<float(res)<<"\tDouble precision="<<res<<"\n";
    n=20;
    res=recursion(n);
    cout<<"n="<<n<<"\tSingle precision="<<float(res)<<"\tDouble precision="<<res<<"\n";
    system("pause");

    return 0;
}

