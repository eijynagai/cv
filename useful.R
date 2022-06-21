# List of useful packages and commands in R


# str_c() concatenate strings
# dir() returns the file/directories contained in a path, similar to ls command
# str_c(dir()) returns the files and you can attach the path to them
# output is a list of paths to the respective files
str_c("path/to/dir", dir("path/do/dir"), sep = '/') 
