# raise number of worker processes
exec { 'raise worker_processes':
  command => "sed -i 's/worker_processes 4;/worker_processes 10;/' /etc/nginx/nginx.conf",
  path    => '/bin',
}
