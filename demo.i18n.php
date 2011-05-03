<?php

/**
 * Internationalization file for the Semantic Maps extension
 *
 * @file SemanticMaps.i18n.php
 * @ingroup Semantic Maps
 *
 * @author Jeroen De Dauw
 */

$messages = array();

/** English
 * @author Jeroen De Dauw
 */
$messages['en'] = array(
	// General
	'semanticmaps-desc' => "Provides the ability to view and edit coordinate data stored with the Semantic MediaWiki extension ([http://mapping.referata.com/wiki/Examples demo's]).",
	'semanticmaps-unrecognizeddistance' => 'The value $1 is not a valid distance.',
	'semanticmaps-kml-link' => 'View the KML file',
	'semanticmaps-kml' => 'KML',
	'semanticmaps-default-kml-pagelink' => 'View page $1',

	// Forms
	'semanticmaps-loading-forminput'	=> 'Loading map form input...',
	'semanticmaps_lookupcoordinates' 	=> 'Look up coordinates',
	'semanticmaps_enteraddresshere' 	=> 'Enter address here',
	'semanticmaps-updatemap' 			=> 'Update map',
	'semanticmaps_notfound' 			=> 'not found',
	'semanticmaps-forminput-remove'		=> 'Remove',
	'semanticmaps-forminput-add'		=> 'Add',
	'semanticmaps-forminput-locations'	=> 'Locations',
	
	// Parameter descriptions
	'semanticmaps_paramdesc_format' 	=> 'The mapping service used to generate the map',
	'semanticmaps_paramdesc_geoservice' => 'The geocoding service used to turn addresses into coordinates',
	'semanticmaps_paramdesc_height' 	=> 'The height of the map, in pixels (default is $1)',
	'semanticmaps_paramdesc_width' 		=> 'The width of the map, in pixels (default is $1)',
	'semanticmaps_paramdesc_zoom' 		=> 'The zoom level of the map',
	'semanticmaps_paramdesc_centre' 	=> 'The coordinates of the maps\' centre',
	'semanticmaps_paramdesc_controls' 	=> 'The user controls placed on the map',
	'semanticmaps_paramdesc_types' 		=> 'The map types available on the map',
	'semanticmaps_paramdesc_type' 		=> 'The default map type for the map',
	'semanticmaps_paramdesc_overlays' 	=> 'The overlays available on the map',
	'semanticmaps_paramdesc_autozoom' 	=> 'If zoom in and out by using the mouse scroll wheel is enabled',
	'semanticmaps_paramdesc_layers' 	=> 'The layers available on the map',
	
	'semanticmaps-par-staticlocations'	=> 'A list of locations to add to the map together with the queried data. Like with display_points, you can add a title, description and icon per location using the tilde "~" as separator.',
	'semanticmaps-par-forceshow'		=> 'Show the map even when there are no locations to display?',
	'semanticmaps-par-showtitle'		=> 'Show a title in the marker info window or not. Disabling this is often usefull when using a template to format the info window content.',
	'semanticmaps-par-centre'		=> 'The centre of the map. When not provided, the map will automatically pick the optimal centre to display all markers on the map.',
	'semanticmaps-par-template'		=> 'A template to use to format the info window contents.'
);

/** Message documentation (Message documentation)
 * @author EugeneZelenko
 * @author Fryed-peach
 * @author Purodha
 * @author Raymond
 */
$messages['qqq'] = array(
	'semanticmaps-desc' => '{{desc}}',
	'semanticmaps-forminput-remove' => '{{Identical|Remove}}',
	'semanticmaps-forminput-add' => '{{Identical|Add}}',
	'semanticmaps-forminput-locations' => '{{Identical|Location}}',
	'semanticmaps_paramdesc_overlays' => 'An "overlay" is a map layer, containing icons or images, or whatever, to enrich, in this case, the map. Could for example be a layer with speed cameras, or municipality borders.',
);

/** Afrikaans (Afrikaans)
 * @author Naudefj
 */
$messages['af'] = array(
	'semanticmaps-desc' => 'Bied die vermoë om koördinaatdata met behulp van die Semantiese MediaWiki-uitbreiding te sien en te wysig ([http://mapping.referata.com/wiki/Examples demo]).',
	'semanticmaps-unrecognizeddistance' => 'Die waarde "$1" is nie \'n geldige afstand nie.',
	'semanticmaps_lookupcoordinates' => 'Soek koördinate op',
	'semanticmaps_enteraddresshere' => 'Voer adres hier in',
	'semanticmaps_notfound' => 'nie gevind nie',
	'semanticmaps_paramdesc_format' => 'Die kaartdiens wat die kaart lewer',
	'semanticmaps_paramdesc_geoservice' => 'Die geokoderingsdiens gebruik om adresse na koördinate om te skakel',
	'semanticmaps_paramdesc_height' => 'Die hoogte van die kaart in spikkels (standaard is $1)',
	'semanticmaps_paramdesc_width' => 'Die breedte van die kaart in spikkels (standaard is $1)',
	'semanticmaps_paramdesc_zoom' => 'Die zoom-vlak van die kaart',
	'semanticmaps_paramdesc_centre' => 'Die koördinate van die middel van die kaart',
	'semanticmaps_paramdesc_controls' => 'Die gebruikerskontroles op die kaart geplaas',
	'semanticmaps_paramdesc_types' => 'Die kaarttipes beskikbaar op die kaart',
	'semanticmaps_paramdesc_type' => 'Die standaard kaarttipe vir die kaart',
	'semanticmaps_paramdesc_overlays' => 'Die oorleggings beskikbaar op die kaart',
	'semanticmaps_paramdesc_autozoom' => 'Of in- en uitzoom met die muis se wiel moontlik is',
	'semanticmaps_paramdesc_layers' => 'Die lae beskikbaar op die kaart',
);