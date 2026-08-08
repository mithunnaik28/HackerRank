#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int N;
    cin>>N;
    vector<int> A(N);

    for (int i = 0; i < N; i++) {
        cin >>A[i];
    }
    
    reverse(A.begin(),A.end());
    
    for(int i=0; i<N;i++){
        cout<<A[i]<<" ";
    }
    return 0;
}
