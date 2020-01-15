#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <iostream>



int rand_range(int start,int end) {
    
    return start + rand() % (end - start + 1);

}

int main() {
    
    std::srand(std::time(nullptr));
    
    const int size{100};
    
    std::vector<int> nums{};
    for(int i=1;i <=size;++i) {
        nums.push_back(rand_range(1,100));

    }


    std::for_each(nums.begin(),nums.end(),[](auto v) {std::cout << v << ' ';});

    std::cout << std::endl;


    std::sort(nums.begin(),nums.end(),[](int x,int y) {return x > y;});


    std::for_each(nums.begin(),nums.end(),[](auto v) {std::cout << v << ' ';});

    std::cout << std::endl;






}
