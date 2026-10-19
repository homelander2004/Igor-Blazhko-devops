#!/bin/bash

echo "===== Student Information ====="
echo "Name: Igor"
echo "Surname: Blazhko"
echo "Group: IT2-2313"
echo "Student ID: 38325"

echo
echo "===== System Information ====="
echo "Current user:"
whoami

echo "Hostname:"
hostname

echo "Current date:"
date

echo "Operating system:"
uname -a

echo "Disk usage:"
df -h

echo "Memory usage:"
free -h

echo
echo "===== File Check ====="

if [ -f "igor_blazhko_info.txt" ]; then
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi
