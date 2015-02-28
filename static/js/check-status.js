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
	var name = roomElem.name;
	if (roomElem.checked){
		$.get( "/light/auto-light" );
	}else{
		$.post( "/light/auto-light");
	}
}

/*function requestStatus(){
	var a = document.getElementsByTagName('label');
	for (var i=0; i<a.length; i++){
		a[i].getAttribute("name");
				//запрос к Arduino и менять статус если надо
		//a[i].innerText=Date();
	} 
}

window.setInterval(requestStatus, 1000);*/