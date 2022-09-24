#Incorrect way of accessing files in python.

```
file = open ('filename.txt')
try :
    file.read()
finally :
    file.close ( )
```

#This import works because we first get the absolute path of the directory of the file and then concatenate to the filename

```
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, 'filename'), "r") as f:
    print(f.read())
```
