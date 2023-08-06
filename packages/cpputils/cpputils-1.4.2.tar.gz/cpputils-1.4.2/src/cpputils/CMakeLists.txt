cmake_minimum_required(VERSION 3.4...3.18)
set(CMAKE_CXX_STANDARD 17)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lib
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
include_directories(${CMAKE_SOURCE_DIR}/lib)
# set(PYTHON_INCLUDE_DIRS ${CMAKE_SOURCE_DIR}/lib)
get_property(
  dirs
  DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  PROPERTY INCLUDE_DIRECTORIES)
foreach(dir ${dirs})
  message(STATUS "dir='${dir}'")
endforeach()

file(GLOB_RECURSE HASH_LIB_SOURCE_FILES
     ${CMAKE_SOURCE_DIR}/lib/hash-library/*.cpp)
list(FILTER HASH_LIB_SOURCE_FILES EXCLUDE REGEX ".*test.*")
# list(APPEND HASH_LIB_SOURCE_FILES ${CMAKE_SOURCE_DIR}/lib/endian2.h)
file(GLOB_RECURSE SOURCE_FILES *.cpp)
pybind11_add_module(cpputils ${SOURCE_FILES} ${HASH_LIB_SOURCE_FILES})

target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_SOURCE_DIR}/lib)
set_target_properties(
  ${PROJECT_NAME} PROPERTIES PUBLIC_HEADER ${CMAKE_SOURCE_DIR}/lib/endian2.h)
set_target_properties(cpputils PROPERTIES OUTPUT_NAME cpputils/_cpputils)
target_compile_definitions(cpputils
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})

add_compile_options(
  "-Wall"
  "-Wpedantic"
  "-Wextra"
  "-fexceptions"
  "$<$<CONFIG:DEBUG>:-O0;-g3;-ggdb>"
  "-Wextra"
  "-Wundef"
  "-pedantic"
  "-msse2"
  "-msse3"
  "-mpopcnt"
  "-funsafe-math-optimizations"
  "-fno-math-errno")
