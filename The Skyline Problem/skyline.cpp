#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

vector<vector<int>> eventscan(const vector<vector<int>> &buildings)
{
    vector<pair<int, int> > events;
    for(const vector<int>& build: buildings) {                  // add events
        events.push_back(make_pair(build[0], -1 * build[2]));   // ensure incoming first
        events.push_back(make_pair(build[1], build[2]));        // outgoing
    }
    sort(events.begin(), events.end());                         // sort by time (x-axis)

    vector<vector<int>> skyline;                                // answer
    multiset<int> heights;                                      // heights stack
    heights.insert(0);                                          // prevent empty stack
    int max_height = 0, curr_height = 0;
    
    for(auto e: events) {
        if(e.second < 0)                                        // incomming
            heights.insert(-1 * e.second);                      // add height stack
        else                                                    // outgoing
            heights.erase(heights.find(e.second));              // remove height stack

        curr_height = *heights.rbegin();                        // current height from stack
        if(curr_height != max_height) {                         // only when new height
            max_height = curr_height;                           // update max height
            skyline.push_back({e.first, curr_height});          // add answer
        }
    }
    
    return skyline;
}

int main()
{
//    vector<vector<int>> buildings = {{2,9,10},{3,7,15},{5,12,12},{15,20,10},{19,24,8}};
    vector<vector<int>> buildings = {{0,2,3},{2,5,3}};
    vector<vector<int>> skyline = eventscan(buildings);
    for (auto point : skyline)
    {
        cout << point[0] << " " << point[1] << " ";
    }
    cout << endl;
}