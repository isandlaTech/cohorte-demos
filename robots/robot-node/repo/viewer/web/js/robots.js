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
	//var tcase = $('#terrain tr:eq('+y_position+') td:eq('+x_position+')');
	console.log("#case-"+x_position+"-"+y_position)
	var x = $("#case-"+x_position+"-"+y_position).offset().left + 4;
	var y = $("#case-"+x_position+"-"+y_position).offset().top + 2
	if (element == "#target") {
		$.getJSON( "/admin/api/target/"+x_position+"-"+y_position, function( data ) {
			$(element).css({ 'left': x + 'px', 'top': y + 'px' });
		});
	} else {
		$(element).css({ 'left': x + 'px', 'top': y + 'px' });
	}
}

function refresh() {
	console.log("refresh...")
	setTimeout(refresh, 2000);
	$.getJSON( "/admin/api/robots", function( data ) {
        for (var i in data['robots']) {
        	var name = data['robots']["name"]
        	var robot = $("#"+name)
        	if (robot == null) {
        		add_robot(name);
        	} else {
        		move_to_position("#"+name, data['robots']["x"], data['robots']["y"]);
        	}

        }
    });
	//move_to_position("#robot-1", 5, 5);
}

$(document).ready(function() {
	var largeur = 10;
	var hauteur = 7;

	generer_terrain(largeur, hauteur);

	add_target();

	//add_robot();

	move_to_position("#target", 3, 3)

	$('td').click(function(){   
	   var $this = $(this);
	   var col   = $this.index();
	   var row   = $this.closest('tr').index();
	   move_to_position("#target", col, row)
	});

	setTimeout(refresh, 2000);
}); 

