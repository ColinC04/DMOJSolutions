#include <bits/stdc++.h>
using namespace std;

int main(){
    int month, day;
    cin >> month >> day;

    string solve = "";
    
    if (month > 2){
        solve = "After";
    }

    if (month == 2 && day > 18){
        solve = "After";
    }

    if (month < 2){
        solve = "Before";
    }

    if (month == 2 && day < 18){
        solve = "Before";
    }

    if (month == 2 && day == 18){
        solve = "Special";
    }

    cout << solve << endl;

}