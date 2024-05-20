iptables -A INPUT -i eno1 -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -i eno1 -p tcp --dport 8000 -j ACCEPT
iptables -A PREROUTING -t nat -i eno1 -p tcp --dport 80 -j REDIRECT --to-port 8000
