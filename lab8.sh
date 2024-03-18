#!/bin/bash
python3 $1
if [ $? -eq 0 ]
then
    echo "Successfully Ran!!!"
else 
    echo "Could not run an error was encountered"
fi

grep -n 'class\|App\|import\|greeting\|1\|main\|def\|275x250' $1


