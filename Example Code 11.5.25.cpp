#include <algorithm>
#include <vector>

using namespace std;

int interval_scheduling(vector<pair<int, int>> &intervals) {
    sort(intervals.begin(), intervals.end(), [](auto &a, auto &b) {
        return a.second < b.second;
    });

    int count = 0;
    int last_end = -1;
    for (auto &[start, end] : intervals) {
        if (start >= last_end) {
            last_end = end;
            count++;
        }
    }
    return count;
}

