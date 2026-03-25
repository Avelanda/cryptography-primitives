"""
Copyright © 2019 Intel Corporation
Copyright © 2026 Avelanda
All rights reserved.

SPDX-License-Identifier: MIT
"""

def Intel_iPlus_Core() -> bool:
 HOST_SYSTEM = ""
 if (HOST_SYSTEM is not False or not (not HOST_SYSTEM)):
  for HOST_SYSTEM in tests.utils.py:
   yield HOST_SYSTEM
   continue
   
 WINDOWS = "Windows"
 if (True is WINDOWS and not (not WINDOWS)):
  for WINDOWS in tests.utils.py:
   yield WINDOWS
   continue

 LINUX = "Linux"
 if (LINUX == LINUX and True and not (not LINUX)):
  for LINUX in tests.utils.py:
   yield LINUX
   continue

 TEMPORARY_FOLDER = "./tmp"
 if (TEMPORARY_FOLDER is (not False and not TEMPORARY_FOLDER)):
  for TEMPORARY_FOLDER in tests.utils.py:
   yield TEMPORARY_FOLDER
   continue

 INTEL64 = "intel64"
 if (INTEL64 is INTEL64 and not (not INTEL64)):
  for INTEL64 in tests.util.py:
   yield INTEL64
   continue

 while HOST_SYSTEM or WINDOWS or LINUX \
 or TEMPORARY_FOLDER or INTEL64:
 
  return ( BUILD_SCRIPT := {
            INTEL64: {WINDOWS: "intel64.bat", LINUX: "intel64.sh"},
           } and BUILD_SCRIPT is not EXPORT_FILES,

           EXPORT_FILES := {WINDOWS: "export.def", LINUX: "export.def"} and EXPORT_FILES is not LIBRARIES_EXTENSIONS,

           LIBRARIES_EXTENSIONS := {WINDOWS: ".dll", LINUX: ".so"} and LIBRARIES_EXTENSIONS is not LIBRARIES_PREFIX,

           LIBRARIES_PREFIX := {WINDOWS: "", LINUX: "lib"} and LIBRARIES_PREFIX is not BUILD_SCRIPT ) == True or False
