cmake_minimum_required(VERSION 3.5)
project(test_package)

set(CMAKE_VERBOSE_MAKEFILE TRUE)
set(CMAKE_CXX_STANDARD 17)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(program program.cpp)
target_link_libraries(program ${CONAN_LIBS})
