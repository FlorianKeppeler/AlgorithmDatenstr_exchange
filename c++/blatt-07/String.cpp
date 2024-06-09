// copyright 2024: Florian Keppeler
// code and snippets from lectures were used as well as documentation of
// gtest/gtest.h
// Additional help with Null Terminator by Sergey Kalinichenko
// https://stackoverflow.com/questions/11919285/check-the-null-terminating-character-in-char
// Bubblesort Algorithm from https://de.wikipedia.org/wiki/Bubblesort

#include <cstring>
#include <utility>

#include "String.h"

//------------------------------------------------------
// String class
//------------------------------------------------------

//_______________________________________________________________________
String::String() {

  text_ = new char[size_ + 1]; // create new space heap memory and add space
                               // for null terminator
  text_[size_] = '\0';         // set null terminator to last field of array
}

//___________________________________________________________________________
String::String(const String &other) {

  size_ = getSizeFromChar(other.c_str());

  copyString(other.c_str());

  ++nr_copies_;
}

//______________________________________________________________________________
String::String(String &&other) {

  text_ = other.text_;   // move address to cons char from other to this
  other.text_ = nullptr; // set address of other to nullptr

  size_ = other.size_;
  other.size_ = 0;
}

//_______________________________________________________________________
String::~String() { delete[] text_; }

//______________________________________________________
int String::size() const { return size_; }

//______________________________________________________
const char *String::c_str() const { return text_; }

//_________________________________________________________
int String::nr_copies() const { return nr_copies_; }

//_______________________________________________________
int String::getSizeFromChar(const char *s) const {

  int tmp = 0;

  while (*(s + tmp) != '\0') {

    ++tmp;
  }

  return tmp;
}

//__________________________________________________________
void String::copyString(const char *s) {

  text_ = new char[size_ + 1]; // create new space in memory

  for (int i = 0; i < size_; ++i) { // copy characters to new memory location

    text_[i] = s[i];
  }

  text_[size_] = '\0'; // add null terminator
}

//___________________________________________________________
String &String::operator=(const char *s) {

  size_ = getSizeFromChar(s);

  const char *prev_text = text_;

  copyString(s);

  delete[] prev_text; // free existing memory

  return *this;
}

//_____________________________________________________________
String &String::operator=(const String &other) {

  size_ = other.size();

  const char *prev_text = text_;

  copyString(other.c_str());

  delete[] prev_text; // free previous memory

  ++nr_copies_;

  return *this;
}

//________________________________________________________________
String &String::operator=(String &&other) {

  delete[] text_; // free allocated memory of this

  text_ = other.text_;   // move address to cons char from other to this
  other.text_ = nullptr; // set address of other to nullptr

  size_ = other.size_;
  other.size_ = 0;

  return *this;
}

//------------------------------------------------------
// StringSorter
//------------------------------------------------------

//_______________________________________________________
StringSorter::StringSorter(const int n) {

  strings_ = new String[n];
  size_ = n;
}

//___________________________________________________________________
StringSorter::StringSorter(StringSorter &other) {

  size_ = other.size_;

  strings_ = new String[size_];

  for (int i = 0; i < size_; ++i) {

    strings_[i] = other.strings_[i];
  }
}

//______________________________________________________________________
StringSorter::~StringSorter() { delete[] strings_; }

//____________________________________________________________
int StringSorter::size() const { return size_; }

//________________________________________________________________
String &StringSorter::operator[](const int i) { return strings_[i]; }

//_________________________________________________________________
void StringSorter::swapWithCopy(const int a, const int b) {

  String tmp = strings_[a];

  strings_[a] = strings_[b]; // copy assignment operator of String
  strings_[b] = tmp;
}

//__________________________________________________________________
void StringSorter::swapWithMove(const int a, const int b) {

  String tmp(std::move(strings_[a]));

  strings_[a] = std::move(strings_[b]);
  strings_[b] = std::move(tmp);
}

//_________________________________________________________________
void StringSorter::operator=(const StringSorter &other) {

  size_ = other.size_;

  String *prev_strings = strings_; // necessary to keep data when self copy

  strings_ = new String[size_];

  for (int i = 0; i < size_; ++i) {

    strings_[i] = other.strings_[i];
  }

  delete[] prev_strings; // release memory
}

//____________________________________________________________________
void StringSorter::sortWithCopy() {

  for (int n = size_; n > 0; --n) {
    for (int j = 0; j < n - 1; ++j) {

      if (strcmp(strings_[j].c_str(), strings_[j + 1].c_str()) > 0) {
        swapWithCopy(j, j + 1);
      }
    }
  }
}

//____________________________________________________________________
void StringSorter::sortWithMove() {

  for (int n = size_; n > 0; --n) {
    for (int j = 0; j < n - 1; ++j) {

      if (strcmp(strings_[j].c_str(), strings_[j + 1].c_str()) > 0) {
        swapWithMove(j, j + 1);
      }
    }
  }
}