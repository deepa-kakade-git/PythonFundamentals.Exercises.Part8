import os

def writeDirTree(dirPath, intoFile):
    with open(intoFile, 'w') as f:
        for root, dirs, files in os.walk(dirPath):
            for file in files:
                filePath = os.path.join(root, file)
                f.write(filePath + '/n')

if __name__ == "__main__":
    dirPath = "/Users/deepa/Documents/Projects/PythonFundamentals.Exercises.Part8"
    output_file = "newFile.txt"
    writeDirTree(dirPath, output_file)

# def writeDirectoryToFile (directory_path , inToFile):
#     with open(inToFile , 'w') as f:
#         for root, directory, files in os.walk(directory_path):  # the os.walk goes thru the directory tree starting from directory path
#             f.write(root + '\n')  #






   # directory_path = (/Users/deepa/Documents/Projects/PythonFundamentals.Exercises.Part8)