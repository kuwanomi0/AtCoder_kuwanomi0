#include <bits/stdc++.h>
using namespace std;

string today_weather;

int main() {
    cin >> today_weather;
    string tomorrow_weather;
    if (today_weather == "Sunny") tomorrow_weather = "Cloudy";
    else if (today_weather == "Cloudy") tomorrow_weather = "Rainy";
    else if (today_weather == "Rainy") tomorrow_weather = "Sunny";
    cout << tomorrow_weather << endl;
}