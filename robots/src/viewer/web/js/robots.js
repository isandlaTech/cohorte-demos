/*
 * COHORTE robots.js
 *
 * Auteur: Bassem DEBBABI
 * Copyright (c) isandlatech.com
 */


function generer_terrain(largeur, hauteur) {
	var terrain = "<table id='terrain' border='1'>"	
	for (var y=0; y<hauteur; y++) {
		terrain += "<tr>";
		for (var x=0; x<largeur; x++) {
			terrain += "<td id='case-"+x+"-"+y+"'>";
			//terrain += "(" + x + ":" + y + ")";
			terrain += "</td>";
		}
		terrain += "</tr>";
	}
  	terrain += "</table>";
  	$("#zone-terrain").html(terrain);
}

function add_target() {
	var target = "<img class='target' id='target' src='imgs/target.png'></img>"
	$("#zone-attente").append(target)
}

function add_robot(name) {
	var robot = "<img class='robot' id='"+name+"' src='imgs/robot.jpg'></img>"
	$("#zone-attente").append(robot)
}

function move_to_position(element, x_position, y_position) {
	var x = $("#case-"+x_position+"-"+y_position).offset().left + 4;
	var y = $("#case-"+x_position+"-"+y_position).offset().top + 2
	if (element == "#target") {
		$.getJSON( "/robots/api/target/"+x_position+"a"+y_position, function( data ) {
			$(element).css({ 'left': x + 'px', 'top': y + 'px' });
		});
	} else {
		$(element).css({ 'left': x + 'px', 'top': y + 'px' });
	}
}

function refresh() {
	setTimeout(refresh, 1000);
	console.log("refresh...")
	$.getJSON( "/robots/api/robots", function( data ) {
		for (var i in data['robots']) {
        	var name = data['robots'][i]["name"]
        	var robot = $("#"+name)
        	if ($("#"+name).length) {
        		console.log("updated robot " + name + " x:" + data['robots'][i]["x"] + " x:" + data['robots'][i]["y"])
        		move_to_position("#"+name, data['robots'][i]["x"], data['robots'][i]["y"]);
        	} else {
        		console.log("new robot " + name)
        		add_robot(name);

        	}
        }
    });
	//move_to_position("#robot-1", 5, 5);
}

$(document).ready(function() {
	var largeur = 15;
	var hauteur = 10;

	generer_terrain(largeur, hauteur);

	add_target();

	//add_robot("robot");

	move_to_position("#target", 3, 3)

	$('td').click(function(){   
	   var $this = $(this);
	   var col   = $this.index();
	   var row   = $this.closest('tr').index();
	   move_to_position("#target", col, row)
	   $('#target').show();
	});
	$('#target').click(function() {
		console.log("target clicked!");
		$.getJSON( "/robots/api/target/-1a-1", function( data ) {
			$('#target').hide();
		});

	});
	setTimeout(refresh, 1000);
}); 

