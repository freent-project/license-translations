import os
import glob
import time
readme = "# FreeNT OpenWindows License\n\nThese are official, localized versions of the OpenWindows license created by the OpenWindows project.\n\n## Languages\n\n"
f = open("readme.md", "w")
for file in glob.glob("*/*.license"):
  readme = readme + "[" + os.path.basename(file).split(".")[0] + "](#" + os.path.basename(file).split(".")[0] + ")\n"
for file in glob.glob("*/*.license"):
  print(file + ":")
  print(open(file, "r").read())
  readme = readme + "\n## " + os.path.basename(file).split(".")[0] + "\n```\n" + open(file, "r").read() + "\n```\n\n"
print("This is what the file will look like AFTER the readme is generated:")
print(readme)
print("Will write README in 3 seconds.")
time.sleep(3)
print("Writing...")
f.write(readme)
print("Closing file...")
f.close()
print("Generated and written README!")
