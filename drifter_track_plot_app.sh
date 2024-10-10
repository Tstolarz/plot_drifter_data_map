#!/bin/bash

# Create an empty array to store the file paths
files=()

# Loop through all the dragged files
for file in "$@"
do
  # Add the file path to the array
  files+=("$file")
done

# Join the file paths with a space separator
file_list=$(IFS=' '; echo "${files[*]}")

# Run the Python script with the list of files
/path/to/python3/with/foilum/installed/ /path/to/drifter_track_plot_app.py $file_list