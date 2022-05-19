#!/bin/bash

# This is a demo script for team 28 group 30 git practice

<<collins
Hello this is a demo script for group 30. We started with a single line comment denoted with number sign #. now using the the multi line comment to pracice
collins
echo "Enter 1st person's name"
read name
if [ $name == Fabrice ]
then
echo "The first person's name is $name"
elif [ $name =! Fabrice ]
then
echo "You've entered the incorrect name"
echo "Reenter the name
read name
elif [ $name == Fabrice ]
echo "You've entered the correct name"
else
echo " This are the individuals that were in our study group"
echo "Fabrice, Cosma, Jumoke, Jennifer, Collins, Chidinma, & Dapo"
echo "Bye"
fi
