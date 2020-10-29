
# Column names and column indices to read

columns = {'date':0, 'time':1, 'tempout':2}

#Dta types for each column (only if non-string) 

types = {'tempout': float}

#Initislize my data variable 
data = {} # list

for column in columns:
    data[column] = [] 

#time = data['time']

# Read the data file 
filename = "data/wxobs20170821.txt"


# 1 way of reading 
#datafile = open(filename, 'r')

#print(datafile.readline()) # reads line 1
#print(datafile.readline()) # reads line 2
#print(datafile.readline()) # reads line 3
#print(datafile.readline()) # reads line 4

# 2 way of reading 
#data = datafile.read() # reads a bunch of lines 
 
#datafile.close()

# 3 way of reading; this way of reading data is recommended because it closes the data for you
with open(filename, 'r') as datafile: # with the file open, i would like to read the file in data
    # read the first 3 lines (header) 
    for _ in range(3): 
        datafile.readline() 
    # Read and parse the rest of the file 
    for line in datafile:
        split_line = line.split() 
        for column in columns: 
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data[column].append(value)

