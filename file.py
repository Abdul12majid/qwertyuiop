import os
import shutil
import stat

def replace_file(file1_name, file1_path, file2_path, new_name):
  """
  Searches for file1 in file1_path, replaces it with file2 from file2_path, renames
  the new file to new_name, and sets its creation date to file2's creation date.

  Args:
    file1_name: Name of the file to search for.
    file1_path: Path to the directory containing file1.
    file2_path: Path to the file to replace file1 with.
    new_name: New name for the replaced file.
  """

  full_path_1 = os.path.join(file1_path, file1_name)
  full_path_2 = os.path.join(file2_path, os.path.basename(file2_path))

  # Check if file1 exists
  if not os.path.exists(full_path_1):
    print(f"File not found: {full_path_1}")
    return

  # Replace file1 with file2
  try:
    shutil.copy2(full_path_2, full_path_1)
    print(f"Replaced {full_path_1} with {full_path_2}")
  except Exception as e:
    print(f"Error replacin file: {e}")
    return

  # Rename the new file
  try:
    os.rename(full_path_1, os.path.join(file1_path, new_name))
    print(f"Renamed {full_path_1} to {os.path.join(file1_path, new_name)}")
  except Exception as e:
    print(f"Error renaming file: {e}")
    return

  # Set creation date of the new file
  try:
    stat_result = os.stat(full_path_2)
    os.utime(os.path.join(file1_path, new_name), (stat_result.st_atime, stat_result.st_mtime))
    print(f"Set creation date of {os.path.join(file1_path, new_name)} to {stat_result.st_ctime}")
  except Exception as e:
    print(f"Error setting creation date: {e}")




file1_name = input("Provide file name: ")  #input name of file to be found
file1_path = "downloads"  #modify to file path

file2_path = "newfolder/newfolder2/"  #modify to file path
print(file2_path)
new_name = input("Provide newfile name: ")  #input newname of file to be found

replace_file(file1_name, file1_path, file2_path, new_name)

