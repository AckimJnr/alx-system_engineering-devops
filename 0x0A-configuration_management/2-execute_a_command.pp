# Manifest version: 1.0.0
# Author: AckimJnr
# Description: kills a running process
exec { 'killmenow':
    command	=>'pkill -f "killmenow"',
    path	=>'/usr/bin:/bin',
    onlyif	=>'pgrep -f "killmenow"',
    refreshonly =>true
}
