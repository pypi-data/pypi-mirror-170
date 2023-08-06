cmake_minimum_required(VERSION 3.22)
project(opuspy)

set(CMAKE_CXX_STANDARD 14)


if (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    # MacOS support.
    list(APPEND CMAKE_PREFIX_PATH /opt/homebrew)
    set(CMAKE_OSX_ARCHITECTURES "arm64")

endif()

# Optimize.
set(CMAKE_CXX_FLAGS " -Wall -O2")

message("heljloj")

# Pybind11
find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG REQUIRED)


# Opus
find_library(Opus_LIBRARIES Opus REQUIRED)
find_path(Opus_INCLUDE_DIRS
        NAMES opus.h
        PATH_SUFFIXES opus
        REQUIRED
)
include_directories(${Opus_INCLUDE_DIRS})

# OpusFile
find_library(OpusFile_LIBRARIES OpusFile REQUIRED)
find_path(
    OpusFile_INCLUDE_DIRS
    NAMES opusfile.h
    PATH_SUFFIXES opus
    REQUIRED
)
include_directories(${OpusFile_INCLUDE_DIRS})

# OpusEnc
find_library(OpusEnc_LIBRARIES OpusEnc REQUIRED)
find_path(
        OpusEnc_INCLUDE_DIRS
        NAMES opusenc.h
        PATH_SUFFIXES opus
        REQUIRED
)
include_directories(${OpusEnc_INCLUDE_DIRS})



pybind11_add_module(opuspy opuspy.cc)
target_link_libraries(opuspy PRIVATE ${OpusFile_LIBRARIES} ${OpusEnc_LIBRARIES})



