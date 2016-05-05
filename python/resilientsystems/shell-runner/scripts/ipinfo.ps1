Param(
  [string]$ipaddr
)

echo "ping:"
ping -n 4 $ipaddr

echo "qwinsta:"
qwinsta /server $ipaddr

echo "nbtstat:"
nbtstat -A $ipaddr

echo "tracert:"
tracert $ipaddr
