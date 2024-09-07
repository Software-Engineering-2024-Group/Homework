#!/bin/bash

# Create post_traces directory if it doesn't exist
mkdir -p post_traces

# Run autopep8
autopep8 --in-place --recursive .
echo "AutoPep8 completed."

# Run flake8 and append the trace
flake8 . >> post_traces/flake8_trace.txt
echo "Flake8 completed."

# Run pylint and append the trace
pylint hw2_debugging.py rand.py >> post_traces/pylint_trace.txt
echo "Pylint completed."