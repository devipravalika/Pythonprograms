def extension(x):
    ext = x.split(".")
    print(ext)
    return (ext[1])


print("Extension of the given file is:", extension("filename.txt"))