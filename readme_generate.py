import os
import glob
import time
from urllib.parse import quote
readme = "# FreeNT OpenWindows License\n\nThese are official, localized versions of the OpenWindows license created by the OpenWindows project.\n\n## List of Languages\n\n"
f = open("readme.md", "w")
for file in sorted(glob.glob("*/*.license")):
  readme = readme + "- [" + os.path.basename(file).split(".")[0] + "](#" + os.path.basename(file).split(".")[0].replace(" ", "-").lower() + ")\n"
readme = readme + "- Not listed? [Submit a language](https://github.com/freent-project/license-translations/issues/new?assignees=&labels=&template=language.yml)!\n"
readme = readme + "## Languages"
for file in sorted(glob.glob("*/*.license")):
  print(file + ":")
  print(open(file, "r").read())
  if os.path.isfile(file.split(".")[0] + ".brl"):
    print("OWL Braille is available in " + os.path.basename(file).split(".")[0] + "! Linking to braille.")
    readme = readme + "\n### " + os.path.basename(file).split(".")[0] + "\n```\n" + open(file, "r").read() + "```\nAlso available as:\n- [Plain text](/" + quote(file) + ")\n- [Braille](/" + quote(file.split(".")[0]) + ".brl" + ")"
  else:
    print("OWL Braille is not available in " + os.path.basename(file).split(".")[0] + ". Linking to plain text only.")
    readme = readme + "\n### " + os.path.basename(file).split(".")[0] + "\n```\n" + open(file, "r").read() + "```\nAlso available as:\n- [Plain text](/" + quote(file) + ")\n- *A braille version is not available for this language.*"
print("This is what the file will look like AFTER the readme is generated:")
print(readme)
print("Will write README in 3 seconds.")
time.sleep(3)
print("Writing...")
f.write(readme)
print("Closing file...")
f.close()
print("Generated and written README!")
