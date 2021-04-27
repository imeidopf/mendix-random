# Requires Python 3

# Built to help with spring cleaning your installed Mendix versions.

# Gets all referenced Mendix versions from the projects in your chosen directory,
# putting them into a list.

import os, xml.etree.ElementTree as ET, re
from pprint import pprint

versionList = []

for root, dirs, files in os.walk("C:\\PATH\\TO\\Mendix"):
    for file in files:
        if file.endswith(".classpath"):
            print("Getting version from: " + os.path.join(root, file))
            tree = ET.parse(os.path.join(root, file))
            root = tree.getroot()
            for classpathentry in tree.findall(".//classpathentry[@kind='lib']")[:1]:
                if not classpathentry.attrib['path'].startswith('C:'): # We only care about the full directory, not paths within the project folders.
                    continue
                v = re.findall(r'Mendix/(.*?)/runtime', classpathentry.attrib['path'])
                if not v in versionList:
                    versionList.append(v)

versionList.sort() # Not perfect but will at least clean up by major version
pprint(versionList)