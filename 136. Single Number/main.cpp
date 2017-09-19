#include <iostream>
#include "solution.h"

// Unit Test

int main() 
{
    Solution s;
    int A1[7] = {1,2,3,5,2,1,3};
	vector<int> A(&A1[0],&A1[6]);
    std::cout << s.singleNumber(A, 7) << std::endl;
    
	return 0;
}
