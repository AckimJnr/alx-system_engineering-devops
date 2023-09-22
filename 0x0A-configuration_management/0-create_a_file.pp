exec { 'file':
    command => '/usr/bin/echo I love Puppet > /tmp/school'
}
exec {'add-permission':
    command => '/usr/bin/chmod 0744 /tmp/school',
    require => Exec['file']
}
exec {'change-owner':
    command => '/usr/bin/chown www-data /tmp/school',
    require => Exec['file']
}
exec {'change-group':
    command => '/usr/bin/chgrp www-data /tmp/school',
    require => Exec['file']
}
