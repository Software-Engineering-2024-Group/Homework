#!/bin/bash
# task1.sh

# Find the process pid of the infinite.sh and kill them.
# 1. ps aux: lists all running processes.
# 2. grep '[i]nfinite.sh': filters the processes to show only the one running infinite.sh
#    a regular expression where [i] is a character class. This means "match the character i."
# 3. awk '{print $2}': extracts the second field, which is the PID.
pid=$(ps aux | grep '[i]nfinite.sh' | awk '{print $2}')

# Terminates the process
if [ -n "$pid" ]; then
    kill $pid
    echo "task1.sh: process infinite.sh with PID $pid has been killed."
else
    echo "task1.sh: No infinite.sh process found."
fi