// copyright 2024: Florian Keppeler
// code and snippets from lectures were used as well as documentation of STL

#include "Points.h"

//______________________________________________________________________
Points::Points() { size_ = 0; }

//___________________________________________________________
void Points::add_coordinate(const float x, const float y) {

  x_.push_back(x);
  y_.push_back(y);

  ++size_;
}

//_________________________________________________________________
std::pair<float, float> Points::get_coordinate(std::size_t index) const {

  std::pair<float, float> coord;

  coord.first = x_[index];
  coord.second = y_[index];

  return (coord);
}

//_______________________________________________________________
std::pair<float, float> Points::operator[](std::size_t index) {

  std::pair<float, float> coord;

  coord.first = x_[index];
  coord.second = y_[index];

  return coord;
}

//_____________________________________________________
std::size_t Points::size() const { return size_; }

//________________________________________________________
std::pair<float, float> Points::get_range_x() const {

  std::pair<float, float> tmp;

  tmp.first = x_[0];
  tmp.second = x_[0];

  for (std::size_t i = 1; i < x_.size(); ++i) {

    if (x_[i] < tmp.first) {
      tmp.first = x_[i];
    }

    if (x_[i] > tmp.second) {
      tmp.second = x_[i];
    }
  }

  return tmp;
}

//______________________________________________________
std::pair<float, float> Points::get_range_y() const {

  std::pair<float, float> tmp;

  tmp.first = y_[0];
  tmp.second = y_[0];

  for (std::size_t i = 1; i < y_.size(); ++i) {

    if (y_[i] < tmp.first) {
      tmp.first = y_[i];
    }

    if (y_[i] > tmp.second) {
      tmp.second = y_[i];
    }
  }

  return tmp;
}
