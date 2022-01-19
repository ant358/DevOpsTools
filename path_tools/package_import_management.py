# %% 
"""
How to import files from different folders
By default, you can't. When importing a file,
Python only searches the current directory,
the directory that the entry-point script is running from,
and sys.path which includes locations such as the package
installation directory (it's actually a little more
complex than this, but this covers most cases).
https://stackoverflow.com/questions/4383571/importing-files-from-different-folder

In vscode you can set the project root which helps
"""

import sys
# check what paths are their already
print(sys.path)

path_to_file = "C:\\Users\\AUSER\\FileLocation\\"
sys.path.insert(1, path_to_file)
# %%
