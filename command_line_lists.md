pwd - print working directory

hostname - my computer’s network name 

mkdir - make directory

cd - change directory

ls - list directory

rmdir - remove directory

pushd -  push directory

popd - popd directory

cp - copy a file or directory

mv - move a file or directory

less - page through a file

cat - print the whole file

xargs - execute arguments

find - find files

grep - find things inside files

man - read a manual page

apropos - find what man page is appropriate 

env - look at your environment

echo - print some arguments

export - export/set a new environment variable 

exit - exit the shell

sudo - DANGER! become super user root DANGER!

--------------------

pwd
# print working directory
# tells you where you are
# directory is a folder

mkdir
# make a directory
mkdir temp
mkdir temp/stuff
mkdir temp/stuff/things
mkdir -p temp/stuff/things/frank/joe/alex/john  # p-path,use / character
mkdir temp/"I have fun"

cd
# change directory
# take you to the folder
cd temp  # take you to the temp folder
cd temp/stuff/things/
cd "I have fun"
cd ..  # move up in the path
cd ../../../
cd ~  # take you home

ls
# list directory
# list the contents of the directory you are currently in

pushd, popd
# pushd save your current location and go to a new location
# popd return to the saved location

touch
# make empty files
touch me.txt

less
# look at the contents of a file
# to get out of less, just type q (as in quit)

cat 
# stream a file
# spew the whole file to the screen with no paging or stopping
# cat can show more files together

cp
# copy a file from one location to anther
# cp -r can copy more directories with files in them
# put a / (slash)at the end of a directory to make sure the file is really a directory.

mv 
# move a file from one location to another
# rename a file : give the old name and the new name

rmdir
# rmdir remove an empty directory
rmdir frank
# rm -rf remove a directory with contents

rm
# remove (delete) a file
# rm -rf recursive remove a directory with files in it.
# Be careful when running recursive remove on files.

exit
# exit your terminal
