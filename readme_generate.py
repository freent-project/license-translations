import os
import glob
import time
readme = "# FreeNT OpenWindows License\n"
f = open("readme.md", "w")
for file in glob.glob("*/*.license"):
  print(file + ":")
  print(open(file, "r").read())
  readme = readme + "\n## " + file = "\n```" + open(file, "r").read() = "\n```\n\n"
print("This is what the file will look like AFTER the readme is generated:")
print(readme)
print("Will write README in 3 seconds.")
time.sleep(3)
print("Writing...")
f.write(readme)
print("Closing file...")
f.close()
print("Generated and written README!")
