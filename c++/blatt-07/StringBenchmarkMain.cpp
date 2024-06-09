
#include <cstdio>
#include <cstdlib>
#include <ctime>

#include <iostream>

#include "String.h"

int main() {

  const int n = 10000;
  const int m = 100;

  StringSorter StrSort1(n);
  StringSorter StrSort2(StrSort1);

  // create n random strings with m characters
  const char *letters = "abcdefghijklmnopqrstuvwxyz";

  for (int j = 0; j < n; ++j) {

    char tmp_str[m + 1];

    for (int i = 0; i < m; ++i) {

      tmp_str[i] =
          letters[rand() % 26]; // draw random letters from the alphabet
    }

    tmp_str[m] = '\0'; // set last field to 0 identifier

    String s1; // create String object to store random string
    s1 = tmp_str;

    StrSort1[j] = tmp_str; // store String object in StringSort objects
    StrSort2[j] = tmp_str;
  }

  // start time measure for sortWithCopy
  clock_t start = clock();

  StrSort1.sortWithCopy();

  clock_t end = clock();

  float elapsed_time1 = 1.0 * (end - start) / CLOCKS_PER_SEC;


  // start time measure for sortWithMove
  start = clock();

  StrSort2.sortWithMove();

  end = clock();

  float elapsed_time2 = 1.0 * (end - start) / CLOCKS_PER_SEC;


  printf("\n\nSort with Copy: %f --- Sort with Move: %f\n\n", elapsed_time1,
         elapsed_time2);

  return 0;
}