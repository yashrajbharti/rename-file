import os

for x in range(36):
    # Absolute path of a file
    old_name = rf'/Users/yashraj/Desktop/Gengar/GengarDex100-{x+1} (dragged).png'
    new_name = rf'/Users/yashraj/Desktop/Gengar/{x+1}.png'
    # Renaming the file
    os.rename(old_name, new_name)