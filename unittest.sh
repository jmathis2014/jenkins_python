#!/bin/bash
#-----------------------------------------------------------------------------#
# A P P  I N F O R M A T I O N #
#-----------------------------------------------------------------------------#
#
# NAME: UNITTEST FOR PYTHON / JENKINS PROJECTS
# DATE: 8/21/2018
# CREATOR: James Mathis
#
# DESCRIPTION:
#
# VERSION: 1.0
#
#-----------------------------------------------------------------------------#

#-----------#
# variables #
#-----------#

UNITTEST_MODULE='unit.test_mymath'

#-----------#
# FUNCTIONS #
#--------------------------------------#

# check if user is ROOT #
function empty() {


}

#--#


#----------#
# MAINLOOP #
#-------------------------------------#

# start uniit testing #
python -B -m $UNITTEST_MODULE -v


#--#

