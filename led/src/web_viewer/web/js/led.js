/*
 * COHORTE led.js
 *
 * Auteur: Bassem DEBBABI
 * Copyright (c) isandlatech.com
 */

function set_led_on(led) {
	console.log("actual state: ON")
	$.getJSON( "/leds/api/leds/"+led+"/on", function( data ) {		
	});
}

function set_led_off(led) {
  console.log("actual state: OFF")	
  $.getJSON( "/leds/api/leds/"+led+"/off", function( data ) {  	
	});
}

function update_actions() {
	$('.switch-input').on('change', function() { 
		var led = $(this).attr('data-led');	
		var state = $(this).attr('data-state');
		console.log("clock on switcher " + led);
		if (state == "on") {
			set_led_off(led)
			$(this).attr('data-state', "off");
		}
		else {
			set_led_on(led)
			$(this).attr('data-state', "on");
		}
	});
}

function refresh() {		
	$.getJSON( "/leds/api/leds", function( data ) {
		frame = ""
		for (var i in data['leds']) {
			var led_name = data['leds'][i]["name"];
			var led_state = data['leds'][i]["state"];
			frame += '<div class="led" id="led-'+led_name+'">'
		    frame += '  <div class="led-name">'+led_name+'</div>'
		    frame += '  <div class="led-switcher">'
		    frame += '  <label id="switcher-zone" class="switch">'
		    frame += '  <input id="switcher" data-led="'+led_name+'" data-state="'+led_state+'" type="checkbox" class="switch-input"' 
		    if (led_state == "on")
		    	frame += '         checked>'
		    else
		    	frame += '         >'
		    frame += '  <span class="switch-label" data-on="On" data-off="Off"></span>'
		    frame += '  <span class="switch-handle"></span>'
		    frame += '  </label>'
		    frame += '  </div>'
		    frame += '</div> '		    

		}
		$('#leds-zone').html(frame);
		update_actions()
    });	
    timer = setTimeout(function() {
    	clearTimeout(timer);
    	refresh();
    }, 1000);
}

var timer;

$(document).ready(function() {	
	timer = setTimeout(refresh, 1000);
	refresh();	
}); 

