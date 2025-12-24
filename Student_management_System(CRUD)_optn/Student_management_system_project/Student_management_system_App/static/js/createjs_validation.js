function checkValidation(){
	let name=document.getElementById("id_name");
	let rollno=document.getElementById("id_rollno");
	let mark=document.getElementById("id_mark");
	let subject=document.getElementById("id_subject");
		let namePattern = /^[A-Za-z ]+$/;
		let markPattern = /^[0-9]+$/;  // only digits allowed



	if(name.value.length<2){
		alert("Minimum 2 charachter should be there in name");
		name.value="";
		name.focus();
		return false;		
	}
	if(!namePattern.test(name.value)){
		alert("Only alphabets allowed in name (no numbers allowed");
		name.value="";
		name.focus();
		return false;		
	}
	if(parseInt(rollno.value)<=0){
		alert("Rollno should minimum 1");
		rollno.value="";
		rollno.focus();
		return false;		
	}
	if(parseInt(mark.value)>100){
		alert("Marks should be not greater than 100");
		mark.value="";
		mark.focus();
		return false;		
	}

	if(!markPattern.test(mark.value)){
    		alert("Only numbers are allowed in Mark field");
    		mark.value = "";
    		mark.focus();
    		return false;
	}



	if(subject.value.length<2){
		alert("Minimum 2 character should be there in subject name");
		subject.value="";
		subject.focus();
		return false;		
	}



return true;
}






