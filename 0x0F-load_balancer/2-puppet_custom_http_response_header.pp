# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Get the hostname dynamically
$hostname = $facts['hostname']

# Create a file with the custom Nginx response header
file { '/etc/nginx/custom-header.conf':
  ensure  => present,
  content => "add_header X-Served-By ${hostname};\n",
}

# Create a symbolic link to enable the custom header configuration
file { '/etc/nginx/sites-enabled/custom-header.conf':
  ensure => link,
  target => '/etc/nginx/custom-header.conf',
  notify => Service['nginx'],
}

# Test Nginx configuration
exec { 'nginx-config-test':
  command => 'nginx -t',
  require => File['/etc/nginx/custom-header.conf'],
}

# Reload Nginx to apply changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/custom-header.conf'],
}

# Create a basic HTML file for testing
file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => 'Hello World!',
  notify  => Service['nginx'],
}

# Start Nginx service
service { 'nginx-start':
  ensure    => running,
  enable    => true,
  require   => File['/var/www/html/index.nginx-debian.html'],
  subscribe => Service['nginx'],
}

notify { 'Script completed successfully.':
  require => Service['nginx-start'],
}
