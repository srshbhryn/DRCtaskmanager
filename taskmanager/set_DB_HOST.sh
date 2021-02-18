export DB_HOST=172.$(ip addr show |grep -w inet |grep -v 127.0.0.1|awk '{ print $2}'| cut -d "/" -f 1 | cut -d "." -f 2).0.1
