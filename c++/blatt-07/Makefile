.SUFFIX:
.PHONY: compile test checkstyle clean format all
.PRECIOUS: %.o

all:  test clean


# CXX = clang++-14 -Wall -Wextra -Wdeprecated -fsanitize=address
# CXX = clang++-14 -Wall -Wextra -Wdeprecated -O3
CXX = clang++ -std=c++14 -Wall -Wextra -Wdeprecated

BASENAME = String

OBJECTS = $(BASENAME)

HEADER = $(addsuffix .h, $(OBJECTS))

TEST_LIBRARIES = -lgtest -lgtest_main -lpthread


$(BASENAME)Test: $(addsuffix .o ,$(BASENAME)Test $(OBJECTS))
	$(CXX) -o $(BASENAME)Test $^ $(TEST_LIBRARIES)

%.o: %.cpp $(HEADER)
	$(CXX) -c $<


$(BASENAME)BenchmarkMain: $(addsuffix .o ,$(BASENAME)BenchmarkMain $(OBJECTS))
	$(CXX) -o $(BASENAME)BenchmarkMain $^

run: compile
	./$(BASENAME)Main

benchmark: $(BASENAME)BenchmarkMain
	./$(BASENAME)BenchmarkMain

test: $(BASENAME)Test
	./$(BASENAME)Test
	

checkstyle:
	clang-format-14 --dry-run -Werror *.cpp *.h

clean:
	rm -f *Main
	rm -f *Test
	rm -f ./*.o

format:
	clang-format -i *.cpp
	clang-format -i *.h