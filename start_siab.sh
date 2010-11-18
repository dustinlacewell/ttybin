#!/bin/bash
/etc/init.d/apache2 restart; 
shellinaboxd -t --service=/:root:root:/var/www/ttybin:"python replay.py -u \${url}"
