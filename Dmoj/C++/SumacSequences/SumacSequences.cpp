#include <bits/stdc++.h>
using namespace std;

int main(){

    // Get inputs for first numbers
    int t1, t2;
    cin >> t1 >> t2;

    bool done = false;
    int counter = 2; 
    while (done == false){

        int nextNum = t1 - t2;

        // Check to see what the values of of next Num are
        if (nextNum >= t2){
            cout << counter << endl;
            done = true;
        }


        //set values for next iteration
        t1 = t2;
        t2 = nextNum;
        counter++;

    }

    return 0;

}