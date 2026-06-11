 #!/bin/bash
#Task 8 - For Loop (Ping 3 Servers)

for ip in 8.8.8.8 1.1.1.1 192.168.1.1;do
	ping -c 1 -W 1 $ip > /dev/null 2>&1

	if [ $? -eq 0 ]; then
		echo "server $ip is up"
	else
		echo "server $ip is dwon"
	fi
done

 
