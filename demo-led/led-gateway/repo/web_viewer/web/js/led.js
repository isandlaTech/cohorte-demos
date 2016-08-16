/*
 * COHORTE led.js
 *
 * Auteur: Bassem DEBBABI
 * Copyright (c) isandlatech.com
 */

var lastupdate = null;
var leds = null;
var cams = null;
var prio = "";

function set_led_on(led) {
	console.log("actual state: ON")
	var debut = new Date().getTime();
	$.getJSON( "/api/leds/"+led+"/on", function( data ) {
		if(data['state'] == "on"){
			$('#switcher-led-'+led).attr('data-updating', "no");
			$('#switcher-led-'+led).attr('data-state', "on");
			var fin = new Date().getTime();
			$('#led-time-response-'+led).html("<p>"+(fin-debut)+" ms</p>");
			console.log(fin-debut);
		}
		$('#switcher-led-'+led).removeAttr("disabled");
	});
}

function set_led_off(led) {
  	console.log("actual state: OFF")
		var debut = new Date().getTime();
  	$.getJSON( "/api/leds/"+led+"/off", function( data ) {
			if(data['state'] == "off"){
				$('#switcher-led-'+led).attr('data-updating', "no");
				$('#switcher-led-'+led).attr('data-state', "off");
				var fin = new Date().getTime();
				$('#led-time-response-'+led).html('<p>'+(fin-debut)+' ms</p>');
				console.log(fin-debut);
			}
			$('#switcher-led-'+led).removeAttr("disabled");
	});
}

function take_cam_pic(cam) {
  	console.log("actual state: taking photo")
		//$('#photo-place-'+cam).html('<img id="photo-'+cam+'" class="photo" src="ajax-loader.gif"/>')
		$('#loader-'+cam).removeClass("hidden");
  	$.getJSON( "/api/cams/"+cam+"/picture", function(data){
			console.log("here1");
			$('#loader-'+cam).addClass("hidden");
			$('#photo-place-'+cam).html('<img id="photo-'+cam+'" class="photo recadre fancybox" src="data:image/png;base64,'+data['res']+'"/>' + '  </div>')
			var addToAll = false;
			var gallery = true;
			var titlePosition = 'inside';
			$(addToAll ? 'img' : 'img.fancybox').each(function(){
					var $this = $(this);
					var title = $this.attr('title');
					var src = $this.attr('data-big') || $this.attr('src');
					var a = $('<a href="#" class="fancybox"></a>').attr('href', src).attr('title', title);
					$this.wrap(a);
			});
			if (gallery)
					$('a.fancybox').attr('rel', 'fancyboxgallery');
			$('a.fancybox').fancybox({
					titlePosition: titlePosition
			});
		}).done(function(  ) {
			console.log("here");
			$('#switcher-cam-'+cam).removeAttr("disabled");
    });
}

function update_actions() {
	$('.switch-input').on('change', function() {
		$(this).attr("disabled", true);
		$(this).attr('data-updating', "yes");
		var led = $(this).attr('data-led');
		var state = $(this).attr('data-state');
		console.log("clock on switcher " + led);
		if (state == "on") {
			set_led_off(led)
		}
		else {
			set_led_on(led)
		}
	});
}

function update_led_actions(led) {
	led.on('change', function() {
		led.attr("disabled", true);
		led.attr('data-updating', "yes");
		var state = led.attr('data-state');
		var name = led.attr('data-led');
		if (state == "on") {
			set_led_off(name)
		}
		else {
			set_led_on(name)
		}
	});
}

function update_cams_actions() {
	$('.switch-cam-input').on('click', function() {
		$(this).attr("disabled", true);
		$(this).attr('data-updating', "yes");
		var state = $(this).attr('data-state');
		var name = $(this).attr('data-cam');
		take_cam_pic(name);
	});
}

function update_cam_actions(cam) {
	cam.on('click', function() {
		var state = cam.attr('data-state');
		var name = cam.attr('data-cam');
		take_cam_pic(name);
	});
}

function refresh() {
	var debut = new Date().getTime();
	$.getJSON( "/api/lastupdate", function( data ) {
		console.log(data);
		console.log(prio);
		if(data['prioritaire']=='yes' && (prio == "no" || prio == "")){
			$('.switch-input').removeAttr("disabled");
      $('.switch-cam-input').removeAttr("disabled");
      $('#connexion-button-p').html("Connecté");
      $('#connexion-button').attr('disable', 'true');
			prio = "yes";
		}
		else if(data['prioritaire']=='no' && (prio == "yes" || prio == "")){
      $('.switch-input').attr("disabled", true);
      $('.switch-cam-input').attr("disabled", true);
      $('#connexion-button-p').html("Non connecté");
      $('#connexion-button').attr('disable', "false");
			prio = "no";
		}
		var fin = new Date().getTime();
		$('#ping-agregateur-p').html('Ping : '+(fin-debut)+' ms');
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
						frame += '	<div class="led-time-switch">'
						if($('#led-time-response-'+led_name).length != 0){
							frame += '  	<div class="led-time-response" id="led-time-response-'+led_name+'">'+$('#led-time-response-'+led_name).html()+'</div>'
						}
						else{
							frame += '  	<div class="led-time-response" id="led-time-response-'+led_name+'"><p>0 ms</p></div>'
						}
            frame += '  	<div class="led-switcher">'
            frame += '    	<label id="switcher-zone" class="switch">'
            frame += '    	<input id="switcher-led-'+led_name+'" data-led="'+led_name+'" data-state="'+led_state+'" data-updating="no" type="checkbox" class="switch-input"'
						if (prio == "no")
                frame += '         disabled="disabled"'
						if (led_state == "on")
                frame += '         checked>'
            else
                frame += '         >'
            frame += '    	<span class="switch-label" data-on="On" data-off="Off"></span>'
            frame += '    	<span class="switch-handle"></span>'
            frame += '    	</label>'
            frame += '  	</div>'
						frame += '  </div>'
            frame += '</div> '
        }
        $('#leds-zone').html(frame);
        update_actions()
    });

		$.getJSON( "/api/cams", function( data ) {
	        frame = ""
	        cams = data;
	        for (var i in data['cams']) {
	            var cam_name = data['cams'][i]["name"];
	            var cam_state = data['cams'][i]["state"];
	            frame += '<div class="cam" id="cam-'+cam_name+'">'
							frame += '	<div class="cam-name-switcher" id="cam-name-switcher-'+cam_name+'">'
	            frame += '  	<div class="cam-name">'+cam_name+'</div>'
            	frame += '  	<div class="cam-switcher">'
            	frame += '    	<label id="switcher-zone" class="button-switch">'
					  	frame += '				<input type="button" id="switcher-cam-'+cam_name+'" data-cam="'+cam_name+'" data-state="'+cam_state+'" data-updating="no" class="switch-cam-input" value="Photo"'
							if (prio == "no")
	                frame += '         disabled="disabled"/>'
							else
									frame += '         />'
							frame += '    	</label>'
            	frame += '  	</div>'
							frame += '  </div>'
							frame += '	<div id="photo-place-'+cam_name+'" class="photo-place">'
							if($('#photo-'+cam_name).length != 0){
								frame += $('#photo-place-'+cam_name).html()
							}
							frame += '  </div>'
							frame += '	<img id="loader-'+cam_name+'" class="loader hidden" src="ajax-loader.gif"/>'
							frame += '</div>'
	        }
	        $('#cams-zone').html(frame);
	        update_cams_actions();
	    });
}

function refresh_leds() {
	if (leds != null) {
		for (var i in leds['leds']) {
	        var led_name = leds['leds'][i]["name"];
	        $.getJSON( "/api/leds/"+led_name, function( data ) {
	        	var led_state = data["state"];
	        	var name = data["name"];
	        	var state = $('#switcher-led-'+name).attr('data-state');
	        	if (state != led_state) {
	        		var updating = $('#switcher-led-'+name).attr('data-updating');
	        		if (updating == "no") {
		        		console.log(">>>>>>>>>> new state for " + name + " -- old:" + state + " --new:" + led_state);
			        	frame = '<div class="led-name">'+name+'</div>'
								frame += '<div class="led-time-switch">'
								if($('#led-time-response-'+name).length != 0){
									frame += '  <div class="led-time-response" id="led-time-response-'+name+'">'+$('#led-time-response-'+name).html()+'</div>'
								}
								else{
									frame += '  <div class="led-time-response" id="led-time-response-'+name+'"><p>0 ms</p></div>'
								}
		            frame += '  <div class="led-switcher">'
		            frame += '  <label id="switcher-zone" class="switch">'
		            frame += '  <input id="switcher-led-'+name+'" data-led="'+name+'" data-state="'+led_state+'" data-updating="no" type="checkbox" class="switch-input"'
								if (prio == "no")
		                frame += '         disabled="disabled"'
								if (led_state == "on")
		                frame += '         checked>'
		            else
		                frame += '         >'
		            frame += '  <span class="switch-label" data-on="On" data-off="Off"></span>'
		            frame += '  <span class="switch-handle"></span>'
		            frame += '  </label>'
		            frame += '  </div>'
								frame += '  </div>'
		            $('#led-'+name).html(frame);
		            update_led_actions( $('#switcher-led-'+name) );
		          }
	          }
	        });
	    }
    }
}

$(document).ready(function(){
  $('#connexion-button').on('click', function() {
    if($('#connexion-button').attr('disable') == "false"){
      $.fancybox('<div style="margin-top:20px;text-align: center;"><div style="margin: auto;display:block;"> <label style="display:inline;">Mot de passe : </label><input type="password" style="display:inline;" id="mdp"/></div><div style="margin:auto;display:block;"><button type="button" style="margin-top:20px;margin-left:auto;margin-right:auto;display:block;" id="co-button"> <p id="co-button-p" style="display:block;"> Connexion </p> </button><p style="margin-top:20px;display:block;" id="res-co-p"></p></div></div>', {
		maxWidth	: 300,
		maxHeight	: 150,
		fitToView	: false,
		autoSize	: false,
		closeClick	: false,
		openEffect	: 'yes',
		closeEffect	: 'yes'
	});
      $('#co-button').on('click', function() {
				if($('#mdp').val() == ""){
					$('#res-co-p').html("Entrez un mot de passe");
				}
				else {
					$.getJSON( "/api/connexion/"+$('#mdp').val(), function( data ) {
	          if(data['prioritaire']=='yes'){
	      			$('.switch-input').removeAttr("disabled");
	            $('.switch-cam-input').removeAttr("disabled");
	            $('#connexion-button-p').html("Connecté");
	            $('#connexion-button').attr('disable', "true");
	            $.fancybox.close(true);
	      		}
	          else{
	            $('#res-co-p').html("Mauvais mot de passe");
	          }
	        });
				}
      });
    }
  });
	load_leds();
	timer = setTimeout(refresh, 1000);
	refresh();
});
