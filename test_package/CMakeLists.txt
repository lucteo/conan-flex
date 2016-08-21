project(TestFlex)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Find Flex in the Conan path
set(CMAKE_PREFIX_PATH ${CONAN_FLEX_ROOT} ${CMAKE_PREFIX_PATH})
find_package(FLEX)

# Add a test grammar
FLEX_TARGET(test-flex basic_nr.l ${CMAKE_CURRENT_BINARY_DIR}/basic_nr.c)
message(STATUS "Flex executable: ${FLEX_EXECUTABLE}")

include_directories( "." )
include_directories( "${CMAKE_CURRENT_BINARY_DIR}" )
add_executable(test-flex ${FLEX_test-flex_OUTPUTS})
target_link_libraries(test-flex m)
