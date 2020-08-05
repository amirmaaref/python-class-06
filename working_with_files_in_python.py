import os
print(os.getcwd())
os.chdir('/Users/amirhosein/Downloads')
print(os.getcwd())

with open('havij_file.mp4') as havij_file:
    print(havij_file.read())