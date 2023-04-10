import os
import subprocess

# Path to TestDisk executable file
testdisk_path = '/usr/bin/testdisk'

# Path to damaged or corrupted disk drive
disk_path = '/dev/sda'

# Path to destination folder to save the recovered files
dest_path = '/home/user/recovered_files/'

# Command to launch TestDisk and analyze the disk
cmd = '{} {}'.format(testdisk_path, disk_path)

# Launch TestDisk and capture the output
output = subprocess.check_output(cmd, shell=True)

# Parse the output to extract the recovered files
recovered_files = []
for line in output.decode('utf-8').split('\n'):
    if 'Recovered' in line:
recovered_files.append(line)

