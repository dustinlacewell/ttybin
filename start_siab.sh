#!/bin/bash
/etc/init.d/apache2 restart; 
shellinaboxd --service=/:root:root:/var/www/ttybin:"python replay.py -u \${url}" --css="white-on-black.css" --debug
