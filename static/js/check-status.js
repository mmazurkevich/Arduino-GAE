function changeElem(checkboxElem) {
	var name =  checkboxElem.name;
	var i = document.getElementsByName(name);	
  if (checkboxElem.checked) {
  	$.get( "/device-helper", { pin: name, type: "On" } );
    i[0].innerText="On"; 
  } else {
  	$.get( "/device-helper", { pin: name, type: "Off" } );
    i[0].innerText="Off";
  }
}

function roomLight(roomElem){
	var name = roomElem.name;
	if (roomElem.checked){
		$.get( "/light/room-light", { room: name, type: "On" } );
	}else{
		$.get( "/light/room-light", { room: name, type: "Off" } );
	}
}

function autoLight(roomElem){
	if (roomElem.checked){
		$.get( "/light/activate-auto", { type: "On", name: "light" } );
	}else{
		$.get( "/light/activate-auto", { type: "Off", name: "light" });
	}
}

function autoClimate(roomElem){
	if (roomElem.checked){
		$.get( "/light/activate-auto", { type: "On", name: "climate" } );
	}else{
		$.get( "/light/activate-auto", { type: "Off", name: "climate" });
	}
}

function secure(roomElem){
	if (roomElem.checked){
		$.get( "/light/activate-auto", { type: "On", name: "secure" } );
	}else{
		$.get( "/light/activate-auto", { type: "Off", name: "secure" });
	}
}
