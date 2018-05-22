nameTextBox = document.getElementById("nameBox");
IDTextBox = document.getElementById("idBox");
gradeTextBox = document.getElementById("gradeBox");
sportsCheckBox = document.getElementById("sportsBox");
internCheckBox = document.getElementById("internBox");
dualCheckBox = document.getElementById("dualBox");
disabilitiesCheckBox = document.getElementById("disabilitiesBox");
otherCheckBox = document.getElementById("otherBox");
distanceTextBox = document.getElementById("distBox");
SubmitButton = document.getElementById("SubmitButton");

SubmitButton.addEventListener("click", OnSubmitClick());


function OnSubmitClick(){
    window.open('0.0.0.0:2107/check/' + nameTextBox.value + '/' + IDTextBox.value + '/' + gradeTextBox.value + '/' + sportsCheckBox.value + '/' + internCheckBox.value + '/' + dualCheckBox.value + '/' + disabilitiesCheckBox.value + '/' + distanceTextBox.value + '/' + otherCheckBox, '_blank');
    alert("hah lol kys");
}

