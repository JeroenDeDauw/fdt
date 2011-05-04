#!/usr/bin/php
<?php

if ( php_sapi_name() != 'cli' ) {
        echo "This script must be run from the command line\n";
        exit( 1 );
}

array_shift( $argv );

require_once $argv[0];

$keys = array();

foreach ( array_keys( $messages ) as $lang ) {
	$keys = array_merge( $keys, array_keys( $messages[$lang] ) );
}

echo implode( "\n", array_unique( $keys ) );

?>