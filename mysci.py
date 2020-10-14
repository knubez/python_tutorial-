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
    data = datafile.read() # dont do tab for indents, do 4 spaces     
    
# data type     
    
# DEBUG
#print(data)
#print(type(data))
#print("data")
