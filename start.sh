#!/bin/bash
/etc/init.d/apache2 restart; 

exitcode=1
user=`whoami`
pwd=`pwd`

while [ $exitcode -ne 0 ]
do
    shellinaboxd --service=/r/:$user:$user:$pwd:"python replay.py -u \${url} -p $pwd" --css="white-on-black.css" --debug
    exitcode=${?}
done

