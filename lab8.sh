#!/bin/bash
python3 $1
grep -n 'class\|App\|import\|greeting' $1

#while read -r output

####if [ output ]
#then
 #  # echo "File does contain $output"
##else 
   # echo " Does not contain class funtion " 

#fi
# ##   echo LINE done <  $INFILE


