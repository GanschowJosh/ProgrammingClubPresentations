#include <iostream>
#include <unordered_map>

int main() {
 std::unordered_map<std::string, int> hashmap;

 hashmap["apple"] = 5;
 hashmap["banana"] = 3;
 hashmap["cherry"] = 7;
 hashmap.erase("cherry");
}