import os

# to be replaced string and file extension filter
search = "file"
replace = "document"

#get all files from current directory
dir_content = os.listdir('.') #Only read current directory
docs = [doc for doc in dir_content if os.path.isfile(doc)]
renamed = 0
    
print(f"{len(docs)} of {len(dir_content)} elements are files.")

#Go through all the files and check if they match the search pattern
for doc in docs:
    #Check if search text is in doc name
    if search in doc:
        #Replace with the given text
        new_name = doc.replace(search, replace)
        os.rename(doc, new_name)
        renamed += 1
        
        print(f"Rename file {doc} to {new_name}")
        
print(f"Renamed {renamed} of {len(docs)} files.")