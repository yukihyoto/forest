#! /usr/bin/env python

# Configurations
# ==============

# Script information
# ------------------

name = 'LO_output_on'

description = 'Set 1st LO SGs output ON.'


# Default parameters
# ------------------

#
# No parameters are available in forest_initialize.
#


# Argument Parser
# ===============

import argparse

p = argparse.ArgumentParser(description=description)

args = p.parse_args()


# Run Script
# ==========

import forest.script

script = forest.script.lo_output_on()
script.run()



