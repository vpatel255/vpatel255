#!/usr/bin/env python3
'''Lab 3 Inv 3 function free_space '''
# Author ID: [157545211]

import subprocess

def free_space():
    # Launch the Linux command: df -h | grep '/$' | awk '{print $4}'
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", 
                            shell=True, capture_output=True, text=True)
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())



import lab3d

print(lab3d.free_space())  # Should return the free space on root directory, e.g., '9.6G'

