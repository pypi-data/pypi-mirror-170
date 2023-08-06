#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "surelog" for configuration "Release"
set_property(TARGET surelog APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(surelog PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/surelog/surelog.lib"
  )

list(APPEND _cmake_import_check_targets surelog )
list(APPEND _cmake_import_check_files_for_surelog "${_IMPORT_PREFIX}/lib/surelog/surelog.lib" )

# Import target "antlr4_static" for configuration "Release"
set_property(TARGET antlr4_static APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(antlr4_static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/surelog/antlr4-runtime-static.lib"
  )

list(APPEND _cmake_import_check_targets antlr4_static )
list(APPEND _cmake_import_check_files_for_antlr4_static "${_IMPORT_PREFIX}/lib/surelog/antlr4-runtime-static.lib" )

# Import target "flatbuffers" for configuration "Release"
set_property(TARGET flatbuffers APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(flatbuffers PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/surelog/flatbuffers.lib"
  )

list(APPEND _cmake_import_check_targets flatbuffers )
list(APPEND _cmake_import_check_files_for_flatbuffers "${_IMPORT_PREFIX}/lib/surelog/flatbuffers.lib" )

# Import target "capnp" for configuration "Release"
set_property(TARGET capnp APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(capnp PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/uhdm/capnp.lib"
  )

list(APPEND _cmake_import_check_targets capnp )
list(APPEND _cmake_import_check_files_for_capnp "${_IMPORT_PREFIX}/lib/uhdm/capnp.lib" )

# Import target "kj" for configuration "Release"
set_property(TARGET kj APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(kj PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/uhdm/kj.lib"
  )

list(APPEND _cmake_import_check_targets kj )
list(APPEND _cmake_import_check_files_for_kj "${_IMPORT_PREFIX}/lib/uhdm/kj.lib" )

# Import target "uhdm" for configuration "Release"
set_property(TARGET uhdm APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(uhdm PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/uhdm/uhdm.lib"
  )

list(APPEND _cmake_import_check_targets uhdm )
list(APPEND _cmake_import_check_files_for_uhdm "${_IMPORT_PREFIX}/lib/uhdm/uhdm.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
