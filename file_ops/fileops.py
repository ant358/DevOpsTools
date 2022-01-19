from pathlib import Path


def get_abs_path(localhome='knownhomedir', pathlist=['folder1',
                                                     'folder2', 
                                                     'targetfile.txt']):
    """To solve the problem of finding files with relative
    paths on windows/linux/mac etc. When a package is deployed 
    on different systems. esp when a module has been
    imported into a different working directory.
    This function finds the absolute path to the current
    working directory cuts it back to the knownhomedir 
    then adds the components of the target pathlist.
    
    Args:
        localhome: str, known home dir such as the app's or repos main folder
        pathlist: list of str, folder and filenames required
        after knownhomedir
    Returns:
         a pathlib object with the absolute path
    """
    p = Path()
    # get the current working dir
    cwd = p.cwd()
    # get the dir tree
    dir_tree = list(cwd.parts)
    # shorten it to the knownhomedir root
    dir_tree = dir_tree[:dir_tree.index(knownhomedir)+1]
    for x in pathlist:
        dir_tree.append(x)
    newpath = Path(*dir_tree)

    return newpath.absolute()
