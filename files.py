import numpy as np
with open("warehouse_data.txt", "w") as f:
    f.write("120\n")
    f.write("85\n")
    f.write("200\n")
    f.write("95\n")
    f.write("150\n")
# If 'w' mode is replaced with 'a' mode:
# 'w' (write mode) overwrites the file every time you run the script.
# 'a' (append mode) adds new data to the end of the file without deleting existing content.
# So on a second run with 'a', the same numbers would be added again, resulting in duplicates.
with open("warehouse_data.txt", "r") as file:
    lines = file.readlines()   # reads all lines into a list

# remove newline characters and print each value
for line in lines:
    value = line.strip()
    print(value)

# Method used: readlines()
# Reason:
# readlines() is suitable because it reads all lines at once into a list,
# making it easy to iterate and process each value.
# read() would return the entire file as one string (harder to split cleanly),
# and readline() reads one line at a time (less convenient for handling all data at once).
with open("warehouse_data.txt", "r") as file:
    values = [line.strip() for line in file]
arr = np.array(values, dtype=int)
print("Array:", arr)
print("Data type:", arr.dtype)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Sum:", np.sum(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
# If one of the values were 'error':
# NumPy would not be able to convert all elements to integers.
# It would either:
# 1. Raise a ValueError (if dtype=int is enforced), or
# 2. Convert the entire array to a string type (dtype='') if dtype is not specified.
# This happens because NumPy arrays require all elements to have the same data type.