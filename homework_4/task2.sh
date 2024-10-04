#!/bin/bash
# task2.sh

# Define the directory where the dataset is located
dataset_dir="dataset1"

# a. 
# 1. Find Files Containing “sample”
grep -rl "sample" "$dataset_dir" | while read -r file; do
    # 2. Count Occurrences of “CSC510”
    count=$(grep -o "CSC510" "$file" | wc -l)
    # 3. Filter Files with at Least 3 Occurrences
    if [ "$count" -ge 3 ]; then
        echo "$count $file"
    fi
# b. Sort the Results
# c. Substitute “file_” with “filtered_”
done | sort -k1,1nr -k2,2 | uniq | awk '{ sub("file_", "filtered_", $2); print }' > filtered_files.txt