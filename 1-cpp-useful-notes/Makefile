CXX = g++
CXXFLAGS = -std=c++14 -Wall -Wextra -O2
TARGET = output
SOURCES = main.cpp
HEADERS = headers/demos/*.h headers/*.h

all: $(TARGET)

$(TARGET): $(SOURCES) $(HEADERS)
	$(CXX) $(CXXFLAGS) $(SOURCES) -o $(TARGET)

clean:
	rm -f $(TARGET) example.txt binary.dat position.txt

.PHONY: all clean
