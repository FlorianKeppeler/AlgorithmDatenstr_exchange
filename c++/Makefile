.SUFFIX:
.PHONY: compile test checkstyle clean format all
.PRECIOUS: %.o

CXX = clang++

HEADERS = $(wildcard *.h)

BASENAME = Snake


all: checkstyle compile test clean

compile: $(BASENAME)Main $(BASENAME)Test


$(BASENAME)Main: $(addsuffix .o, $(BASENAME)Main $(BASENAME))
	$(CXX) -o $@ $^ -lncurses

$(BASENAME)Test: $(addsuffix .o, $(BASENAME)Test $(BASENAME))
	$(CXX) -o $@ $^ -lncurses -lgtest -lgtest_main

%.o: %.cpp $(HEADERS)
	$(CXX) -c $<


test: $(BASENAME)Test
	./$(BASENAME)Test


checkstyle:
	clang-format-14 --dry-run -Werror *.cpp *.h

clean:
	rm -f *Main
	rm -f *Test
	rm -f ./*.o

format:
	clang-format-14 -i *.cpp
	clang-format-14 -i *.h