// copyright 2024: Florian Keppeler
// code and snippets from lectures were used as well as documentation of STL

#include "HeatMap.h"
#include "TerminalManager.h"

//__________________________________________________________________
void HeatMap::readPointsFromFile(const std::string &filename) {

  std::ifstream file(filename);
  std::string line;

  double x_tmp;
  double y_tmp;

  std::size_t begin;

  while (std::getline(
      file,
      line)) { // every time getline is executed it jumps to the next line in
               // file when there is no line left to read getline returns 0

    // get x coordinate from file
    begin = line.find('(');
    x_tmp = std::stod(line.data() + begin + 1);

    // get y coordinate from file
    begin = line.find(' ');
    y_tmp = std::stod(line.data() + begin + 1);

    // add x and y coordinate to Points object
    points_.add_coordinate(x_tmp, y_tmp);
  }
}

//____________________________________________________________________________
std::size_t HeatMap::size() const { return points_.size(); }

//_____________________________________________________________________________
std::pair<float, float> HeatMap::get_coordinate(std::size_t index) const {

  return points_.get_coordinate(index);
}

//____________________________________________________________________________
void HeatMap::computeHeatMap(std::size_t numRows, std::size_t numCols) {

  // temporary variables
  std::pair<float, float> range_x = points_.get_range_x();
  std::pair<float, float> range_y = points_.get_range_y();

  float x_by = (range_x.second - range_x.first) / numCols;  // get interval for pixels
  float y_by = (range_y.second - range_y.first) / numRows;

  float scaling  = 0.6; // scaling to represent the map less distorted

  std::size_t tmp_col;
  std::size_t tmp_row;

  std::pair<float, float> tmp_coord;

  std::unordered_map<size_t, size_t> points_per_pixel_tmp;


  // count points per pixel
  for (std::size_t i = 0; i < points_.size(); ++i) {

    tmp_coord = points_.get_coordinate(i);

    tmp_col = std::size_t((tmp_coord.first - range_x.first) * scaling / x_by); // defines column in which the point is located  

    tmp_row = std::size_t((tmp_coord.second - range_y.first)  / y_by); // defines row in which the point is located

    points_per_pixel_tmp[tmp_col + (numRows - tmp_row) * numCols]++;  // transform columns and rows in one dimensional index
  }

  // is not necessary but I thought it would be interesting to play around with vectors and maps

  for (const std::pair<std::size_t, std::size_t> points_count :
       points_per_pixel_tmp) {

    points_per_pixel_.push_back(points_count);  // transform unordered_map data in a vector
  }

  std::sort(points_per_pixel_.begin(), points_per_pixel_.end());  // is not necessary but i wanted to experiment with sort and iterators, also helps with debugging
}

//_______________________________________________________________________________
void HeatMap::normalizeHeatMap() {

  size_t max_tmp = 0;
  size_t min_tmp = 0;

  max_tmp = points_per_pixel_[0].second;
  min_tmp = points_per_pixel_[0].second;

  // calculate minimum and maximum of points per pixel
  for (std::size_t i = 1; i < points_per_pixel_.size(); ++i) {

    if (points_per_pixel_[i].second > max_tmp) {

      max_tmp = points_per_pixel_[i].second;
    }

    if (points_per_pixel_[i].second < min_tmp) {

      min_tmp = points_per_pixel_[i].second;
    }
  }

  max_tmp -= min_tmp; // since should be 0 the minimum number of points per pixel, maximum must be modified to receive 1 for the maximum number of points

  std::pair<size_t, float> tmp_pair;

  for (std::size_t i = 0; i < points_per_pixel_.size(); ++i) {

    tmp_pair.first = points_per_pixel_[i].first;
    tmp_pair.second = (points_per_pixel_[i].second - min_tmp) / float(max_tmp);  // normalize points per pixel in [0, 1] (minimum points per pixel, maximum points per pixel)

    points_per_pixel_normalized_.push_back(tmp_pair);
  }
}

//___________________________________________________________________
void HeatMap::drawHeatMap(TerminalManager *terminal_manager) {

  int tmp_col;
  int tmp_row;

  UserInput input;

  // start drawing to terminal
  while (true) {  

      for (const auto &pair : points_per_pixel_normalized_) {

        tmp_col = pair.first % terminal_manager->numCols();  // get columns from one dimensional index
        tmp_row = pair.first / terminal_manager->numCols();  // get rows from one dimensional index

        terminal_manager->drawPixel(tmp_row, tmp_col, true, pair.second);
      }
    
    input = terminal_manager->getUserInput();

    if (input.keycode_ == 113) {  // exit drawing loop when 'q' is pressed
      break;
    }

    terminal_manager->refresh();
    usleep(50000);
  }
}