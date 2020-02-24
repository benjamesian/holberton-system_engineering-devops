# remove file limits for holberton user
exec { 'remove holberton hard nofile':
  command => "sed -e '/holberton hard nofile/ s/^#*/#/' -i /etc/security/limits.conf",
  path    => '/bin',
}
exec { 'remove holberton soft nofile':
  command => "sed -e '/holberton soft nofile/ s/^#*/#/' -i /etc/security/limits.conf",
  path    => '/bin',
}
