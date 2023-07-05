import os

# Specify the root directory path
root_directory = os.environ['DATASET']

# Recursive function to rename files
def rename_files(directory):
    # Get the list of files in the directory
    files = os.listdir(directory)

    # Iterate over each file in the directory
    for file in files:
        # Construct the current file path
        current_path = os.path.join(directory, file)

        # Check if the current item is a file
        if os.path.isfile(current_path):
            # Check if the file ends with ".csv"
            if file.endswith(".csv"):
                # Generate the new file name with ".txt" extension
                new_name = os.path.splitext(file)[0] + ".txt"
                
                # Construct the new file path
                new_path = os.path.join(directory, new_name)
                
                # Rename the file
                os.rename(current_path, new_path)
                
                print(f"Renamed {file} to {new_name}")
        
        # Check if the current item is a directory
        elif os.path.isdir(current_path):
            # Recursively call the function for subdirectories
            rename_files(current_path)

# Call the function with the root directory
if __name__ == "__main__":
    rename_files(root_directory)
    print("File renaming completed!")


