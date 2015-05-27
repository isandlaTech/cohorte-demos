/*
 * COHORTE led.js
 *
 * Auteur: Bassem DEBBABI
 * Copyright (c) isandlatech.com
 */

var lastupdate = null;
var leds = null;

function set_led_on(led) {
	console.log("actual state: ON")	
	$.getJSON( "/api/leds/"+led+"/on", function( data ) {		
		$('#switcher-'+led).attr('data-updating', "no");
	});
}

function set_led_off(led) {	
  	console.log("actual state: OFF")	  
  	$.getJSON( "/api/leds/"+led+"/off", function( data ) {  	
  		$('#switcher-'+led).attr('data-updating', "no");
	});
}

function update_actions() {	
	$('.switch-input').on('change', function() { 		
		$(this).attr('data-updating', "yes");
		var led = $(this).attr('data-led');	
		var state = $(this).attr('data-state');		
		console.log("clock on switcher " + led);
		if (state == "on") {
			$(this).attr('data-state', "off");
			set_led_off(led)			
		}
		else {
			$(this).attr('data-state', "on");
			set_led_on(led)
			
		}		
	});
}

function update_led_actions(led) {	
	led.on('change', function() { 	
		led.attr('data-updating', "yes");	
		var state = led.attr('data-state');	
		var name = led.attr('data-led');	
		if (state == "on") {
			led.attr('data-state', "off");
			set_led_off(name)			
		}
		else {
			led.attr('data-state', "on");
			set_led_on(name)			
		}		
	});
}

function refresh() {	
	
	$.getJSON( "/api/lastupdate", function( data ) {
		var tmp = data['lastupdate'];
		if (lastupdate == null) {
			lastupdate = tmp;
		}
		if (tmp != lastupdate) {
			lastupdate = tmp;
			load_leds();
		} else {
			refresh_leds();
		}
	});		
    timer = setTimeout(function() {
    	clearTimeout(timer);
    	refresh();
    }, 1000);
}

var timer;

function load_leds() {	
	$.getJSON( "/api/leds", function( data ) {
        frame = ""
        leds = data;
        for (var i in data['leds']) {
            var led_name = data['leds'][i]["name"];
            var led_state = data['leds'][i]["state"];
            frame += '<div class="led" id="led-'+led_name+'">'
            frame += '  <div class="led-name">'+led_name+'</div>'
            frame += '  <div class="led-switcher">'
            frame += '    <label id="switcher-zone" class="switch">'
            frame += '    <input id="switcher-'+led_name+'" data-led="'+led_name+'" data-state="'+led_state+'" data-updating="no" type="checkbox" class="switch-input"'
            if (led_state == "on")
                frame += '         checked>'
            else
                frame += '         >'
            frame += '    <span class="switch-label" data-on="On" data-off="Off"></span>'
            frame += '    <span class="switch-handle"></span>'
            frame += '    </label>'
            frame += '  </div>'
            frame += '</div> '
        }
        $('#leds-zone').html(frame);
        update_actions()
    });
}

function refresh_leds() {	
	if (leds != null) {
		for (var i in leds['leds']) {			
	        var led_name = leds['leds'][i]["name"];	             	        
	        $.getJSON( "/api/leds/"+led_name, function( data ) {
	        	var led_state = data["state"];	 
	        	var name = data["name"];  
	        	var state = $('#switcher-'+name).attr('data-state');
	        	if (state != led_state) {
	        		var updating = $('#switcher-'+name).attr('data-updating');
	        		if (updating == "no") {	
		        		console.log(">>>>>>>>>> new state for " + name + " -- old:" + state + " --new:" + led_state); 
			        	frame = '  <div class="led-name">'+name+'</div>'
			            frame += '  <div class="led-switcher">'
			            frame += '  <label id="switcher-zone" class="switch">'
			            frame += '  <input id="switcher-'+name+'" data-led="'+name+'" data-state="'+led_state+'" data-updating="no" type="checkbox" class="switch-input"'
			            if (led_state == "on")
			                frame += '         checked>'
			            else
			                frame += '         >'
			            frame += '  <span class="switch-label" data-on="On" data-off="Off"></span>'
			            frame += '  <span class="switch-handle"></span>'
			            frame += '  </label>'
			            frame += '  </div>'
			            $('#led-'+name).html(frame);
			            update_led_actions( $('#switcher-'+name) );
		            }
	            }
	        });	       
	    }    
    }
}

$(document).ready(function() {	
	load_leds();
	timer = setTimeout(refresh, 1000);
	refresh();	

}); 

