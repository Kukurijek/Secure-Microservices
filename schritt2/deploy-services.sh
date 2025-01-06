#!/bin/bash

# Set the list of directories containing YAML files
directories=("billing-db" "mysql" "radius-service")

# Loop through each directory and apply all YAML files
for dir in "${directories[@]}"; do
    echo "Applying YAML files in directory: $dir"
    kubectl apply -f "$dir/"
    if [ $? -eq 0 ]; then
        echo "Successfully applied YAML files in $dir"
    else
        echo "Failed to apply YAML files in $dir" >&2
        exit 1
    fi
done

echo "All services have been successfully deployed!"
