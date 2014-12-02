/*
 * COHORTE led.js
 *
 * Auteur: Bassem DEBBABI
 * Copyright (c) isandlatech.com
 */

function set_led_on() {
	console.log("actual state: ON")
	$.getJSON( "/leds/api/led/on", function( data ) {
		$('switcher').prop('checked', true);
	});
}

function set_led_off() {
  console.log("actual state: OFF")	
  $.getJSON( "/leds/api/led/off", function( data ) {
  	$('switcher').prop('checked', false);
	});
}

$('#switcher').on('change', function() { 
    var state = this.checked;
    if (state == true) {
    	set_led_on();
    } else {
    	set_led_off();
    }
});

function refresh() {
	setTimeout(refresh, 1000);
	console.log("refresh...")
	$.getJSON( "/leds/api/led", function( data ) {
			var state = data["state"];			
			if (state == null) {
				$("#switcher-zone").hide();
				console.log("state: null")
			} else {
				console.log("state: " + state);
				if (state == "on") {
					$('#switcher').prop('checked', true);
					$("#switcher-zone").show();
				} else if (state == "off") {
					$('#switcher').prop('checked', false);
					$("#switcher-zone").show();
				} else {
					$("#switcher-zone").hide();
				}
			}
    });
	//move_to_position("#robot-1", 5, 5);
}

$(document).ready(function() {
	$("#switcher-zone").hide();
	setTimeout(refresh, 1000);
}); 

