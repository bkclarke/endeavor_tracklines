import os

# Function to remove a specific word from filenames in a directory
def remove_word_from_filenames(directory, word):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Iterate through each file
    for filename in files:
        # Construct the full file path
        filepath = os.path.join(directory, filename)
        
        # Check if the file is a regular file
        if os.path.isfile(filepath):
            # Split the filename and extension
            name, ext = os.path.splitext(filename)
            
            # Check if the word exists in the filename
            if word in name:
                # Remove the word from the filename
                new_name = name.replace(word, "")
                
                # Construct the new file path
                new_filepath = os.path.join(directory, new_name + ext)
                
                # Rename the file
                os.rename(filepath, new_filepath)
                print(f"Renamed '{filename}' to '{new_name + ext}'")

# Specify the directory and word to remove
directory = "C:/Users/bonny/github/endeavor_tracklines/kml_files"
word_to_remove = "-"

# Call the function
remove_word_from_filenames(directory, word_to_remove)