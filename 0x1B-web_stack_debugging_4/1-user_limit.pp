# update file access limits for user holberton
exec { 'hard_limits_conf':
  command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 4096/" /etc/security/limits.conf',
  provider => 'shell',
}
exec { 'soft_limits_conf':
  command  => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4096/" /etc/security/limits.conf',
  provider => 'shell'
}
