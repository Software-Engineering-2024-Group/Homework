# Use awk to process the titanic.csv file
awk -F, '
# Filter for passengers in 2nd class who embarked at Southampton
$3 == 2 && $13 ~ /^[[:space:]]*S[[:space:]]*$/ {
    # Replace 'male' with 'M' and 'female' with 'F'
    if ($6 == "male") 
        $6 = "M"; 
    else if ($6 == "female") 
        $6 = "F"; 
    
    # Check if Age (7th column) is not empty
    if ($7 != "") { 
        # Sum the ages for average calculation
        age_sum += $7; 
        # Increment the count of valid age entries
        count++;
    }
} 
# At the end of processing the file
END { 
    # Check if we found any passengers
    if (count > 0) 
        # Print the average age
        print "Average Age:", age_sum/count; 
    else 
        # Print a message if no passengers wgit ere found
        print "No passengers found."
}' titanic.csv
