#fix wp-settings file
exec {'fix_wp_settings':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => 'shell',
}
