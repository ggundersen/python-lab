"""This module parses a GEO DataSet SOFT file.
"""

# Open the soft file and initialize an empty list.
dataset = open('GDS1001.soft', 'r')
lines = []

# Iterate over every line in the file, storing it in the list.
for line in dataset:
    lines.append(line)

# Remove metadata
idx = lines.index('!dataset_table_begin\n')
lines = lines[idx+1:]

# Remove the newline character and split on the tab.
lines = [line[:-1].split('\t') for line in lines]

# Remove the first element from every list.
lines = [line[1:] for line in lines]

# Remove lines with null expression values or invalid gene symbols.
out = open('out.txt', 'w+')
for line in lines:
    if 'null' in line or '--Control' in line:
        continue
    if len(line) == 0:
        continue
    # Set string to uppercase.
    line[0] = line[0].upper()
    # Convert list to tab-separated string with newline character
    line = '\t'.join(line) + '\n'
    out.write(line)

# Close the files.
dataset.close()
out.close()
