// copyright 2024: Florian Keppeler
// code and snippets from lectures were used as well as documentation of
// gtest/gtest.h
// Additional help with Null Terminator by Sergey Kalinichenko
// https://stackoverflow.com/questions/11919285/check-the-null-terminating-character-in-char
// Bubblesort Algorithm from https://de.wikipedia.org/wiki/Bubblesort

#pragma once

class String {

private:
  char *text_;

  int size_ = 0;

  int nr_copies_ = 0; // just to check if move constructor does not actually
                      // call copy constructor

public:
  // constructor
  explicit String();

  // copy constructor
  String(const String &other);

  // move constructor
  String(String &&other);

  // destructor
  ~String();

  // get size of character array
  int getSizeFromChar(const char *s) const;

  // copy character array in string
  void copyString(const char *s);

  // assignment operator
  String &operator=(const char *s);

  // copy assignment operator
  String &operator=(const String &other);

  // move assignent operator
  String &operator=(String &&other);

  // get size of String object
  int size() const;

  // get string
  const char *c_str() const;

  // get nr_copies
  int nr_copies() const;
};

class StringSorter {

private:
  int size_ = 0;

  String *strings_;

public:
  // constructor
  StringSorter(const int n);

  // copy constructor
  StringSorter(StringSorter &other);

  // destructor
  ~StringSorter();

  // returns number of String objects
  int size() const;

  // [] operator to access String objects
  String &operator[](const int i); // needs to return a reference in order to
                                   // modify String objects in StringSorter

  // copy assignment operator
  void operator=(const StringSorter &other);

  // swaps String object at a with string at b by copying String objects
  void swapWithCopy(const int a, const int b);

  // swaps String object at a with string at b by moving String objects
  void swapWithMove(const int a, const int b);

  // sorts String objects via Bubblesort algorithm and copy constructor
  void sortWithCopy();

  // sorts String objects via Bubblesort algorithm and move constructor
  void sortWithMove();
};