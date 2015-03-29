
function requestStatus(){
	var a = document.getElementsByTagName('label');
	var ip = "192.168.1.98";
	[].forEach.call(a,function (curValue) {
		$.get("http://"+ip+"/digital/"+curValue.getAttribute("name"),function(data){
			var c = curValue.getAttribute("name")
			var b = document.getElementsByName(c);
			if (data.return_value == 0){
  				curValue.innerText="On";
  				b[1].checked = true;
  			}else{
  				curValue.innerText="Off";
  				b[1].checked = false;
  			}
		});
	});
}

window.setInterval(requestStatus, 3000);