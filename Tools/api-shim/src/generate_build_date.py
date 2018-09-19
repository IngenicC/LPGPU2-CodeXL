#
# The MIT License
#
# Copyright (c) 2016 Samsung Electronics Co., Ltd. All Rights Reserved
# For conditions of distribution and use, see the accompanying COPYING file.
#
#
import sys
import datetime

def writeBuildDateFile(cpp_filename, cpp):
    cpp.write('''
//
// Auto generated by {}
//
const char* BUILD_DATE = "{}";

'''.format(sys.argv[0], datetime.datetime.isoformat(datetime.datetime.now(), " ")))

def getConfiguration():
    import argparse
    from os.path import expanduser as expandUser

    # allow a config file to override the defaults
    parser = argparse.ArgumentParser(description="LPGPU2 date file generator")

    defaults = {"cpp": "",
                }

    parser.set_defaults(**defaults)

    parser.add_argument("--cpp", type=str, help="Cpp filename. Default is stdout")

    ns = parser.parse_args()

    if ns.cpp:
        ns.append = expandUser(ns.cpp)

    return ns


if __name__ == "__main__":
    import sys

    config = getConfiguration()

    if config.cpp:
        cpp_filename = config.cpp
        cpp = open(config.cpp, "w")
    else:
        cpp_filename = ""
        cpp = sys.stdout

    writeBuildDateFile(cpp_filename, cpp)
