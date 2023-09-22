# Manifest version: 1.0.0
# Author: AckimJnr
# Description: kills a running process
exec { 'killmenow':
    command => '/usr/bin/pkill -f "killmenow"'
}
