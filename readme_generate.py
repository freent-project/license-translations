import os
import glob
import time
readme = "# FreeNT OpenWindows License\n\nThese are official, localized versions of the OpenWindows license created by the OpenWindows project.\n\n## List of Languages\n\n"
f = open("readme.md", "w")
for file in sorted(glob.glob("*/*.license")):
  readme = readme + "- [" + os.path.basename(file).split(".")[0] + "](#" + os.path.basename(file).split(".")[0].replace(" ", "-").lower() + ")\n"
readme = readme + "- Not listed? [Submit a language](https://github.com/freent-project/license-translations/issues/new?assignees=&labels=&template=language.yml)!\n"
readme = readme + "## Languages"
for file in sorted(glob.glob("*/*.license")):
  print(file + ":")
  print(open(file, "r").read())
  readme = readme + "\n### " + os.path.basename(file).split(".")[0] + "\n```\n" + open(file, "r").read() + "```\nYou can get a copy of this license as text [here](/" + file + ") or ~~Braille~~ (*not yet, but soon*)."
print("This is what the file will look like AFTER the readme is generated:")
print(readme)
print("Will write README in 3 seconds.")
time.sleep(3)
print("Writing...")
f.write(readme)
print("Closing file...")
f.close()
print("Generated and written README!")
