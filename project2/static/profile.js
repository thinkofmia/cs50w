/**
 * profile.js
 * The Main JS file to store all the codes and functions 
 */

var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

//Choosing a certain profile pic
function selectPic(choice){
    console.log("Clicked profile pic "+choice);
    //Update profile pic and save on server
    socket.emit('changePic', {"user": getDisplayName(), "choice": choice});
    //Get all the pics
    var allpics = document.querySelectorAll(".displaypic");
    //Remove active class from all the pics
    for (var i=0;i<allpics.length;i++){
        allpics[i].classList.remove("active");
    }
    //Add active class to the selected pic
    allpics[choice-1].classList.add("active");
}

//Update user's selection
function updateSelection(){
    //Get json data of profiles
    var data = document.querySelector('#profilesdata').innerHTML;
    data_array = JSON.parse(data);
    //Loop for all profiles
    for (var name in data_array){
        //If profile belongs to user
        if (name == getDisplayName()){
            //Selects for the user the current option
            selectPic(data_array[name]);
        }
    }
}

//Runs onload
document.addEventListener('DOMContentLoaded', () => {
    updateSelection();
    //Update pics
    socket.on('updatePic', data => {
        //Update json data of profiles
        var pictures = document.querySelector('#profilesdata');
        pictures.innerHTML = data;
        console.log(data);
    });
});
