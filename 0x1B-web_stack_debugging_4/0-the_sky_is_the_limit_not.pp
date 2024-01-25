# update rate limit

exec { 'update_request_limit':
  command  => 'sed -i "s|ULIMIT=\"-n 15\"|ULIMIT=\"-n 10000\"|" /etc/default/nginx && service nginx restart',
  provider => 'shell',
}
