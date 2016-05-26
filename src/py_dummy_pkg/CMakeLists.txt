cmake_minimum_required(VERSION 2.8.3)
project(py_dummy_pkg)

find_package(catkin REQUIRED)

catkin_python_setup()
catkin_package()

### HACK to make package_data work in devel
add_custom_target(_py_package_data_symlink ALL
  COMMAND ${CMAKE_COMMAND} -E create_symlink
    ${CMAKE_CURRENT_SOURCE_DIR}/src/${PROJECT_NAME}/data
    ${CATKIN_DEVEL_PREFIX}/${PYTHON_INSTALL_DIR}/${PROJECT_NAME}/data
)
###

install(PROGRAMS
  scripts/runner.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
