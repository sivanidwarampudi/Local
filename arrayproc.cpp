#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <cstdlib>

int processArray(std::vector<int> &array) {
  /* 
   * Do not make any changes outside this function.
   *
   * Modify this function to process `array` as indicated
   * in the question. At the end, return the length of the
   * array.
   *
   * Do not print anything in this function
   * Do not write anything to the standard output
   *
   * Submit this entire program (not just this function)
   * as your answer
   */
  return array.size();
}

int main(void) {
  std::vector<int> array;
  int val;
  while (std::cin >> val) {
    array.push_back(val);
  }
  for(std::vector<int>::iterator a = array.begin(); a != array.end(); a++) {
    std::cout << *a << std::endl;
  }
  return 0;
}

