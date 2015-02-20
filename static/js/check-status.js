function changeElem(checkboxElem) {
	var name =  checkboxElem.name;
	var i = document.getElementsByName(name);	
  if (checkboxElem.checked) {
  	//request to Arduino
    i[0].innerText="On"; 
  } else {
  	//request to Arduino
    i[0].innerText="Off";
  }
}

function requestStatus(){
	var a = document.getElementsByTagName('label');
	for (var i=0; i<a.length; i++){
		a[i].getAttribute("name");
				//запрос к Arduino и менять статус если надо
		//a[i].innerText=Date();
	} 
}

window.setInterval(requestStatus, 1000);