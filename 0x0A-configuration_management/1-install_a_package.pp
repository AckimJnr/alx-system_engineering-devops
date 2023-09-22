# Manifest version: 1.0.0
# Author: AckimJnr
# Description: Installs flass from pip3

package{'flask':
    ensure  => 'installed',
    require => Exec['install-flask']
}
exec {
    'install-flask':
    command => '/usr/bin/pip3 install Flask==2.1.0'
}
