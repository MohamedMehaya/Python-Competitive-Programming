#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int main() {
    int n;
    cin >> n; cin.ignore();
    vector<string> names_degrees(n);

    for (int i = 0; i < n; i++) {
        getline(cin, names_degrees[i]);
    }

    for (int i = 0; i < n; i++) {
        stringstream ss(names_degrees[i]);
        string name, degree;
        getline(ss, name, ',');
        ss >> degree;

        if (!degree.empty()) {
            cout << degree << endl;
        } else {
            cout << "degree not present" << endl;
        }
    }

    return 0;
}
