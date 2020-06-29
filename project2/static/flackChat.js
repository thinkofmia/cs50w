/**
 * flackChat.js
 * The Main JS file to store all the codes and functions 
 */

var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

//Gets last browsed channel
function getLastChannel(){
    //Get from local storage
    var result = localStorage.getItem('lastChannel');
    //Returns null if doesnt exists or invalid
    if (result == null) return null;
    else if (result.length <=0) return null;
    //Else return the string
    else return result;
}

//Remove last browsed channel
function clearLastChannel(){
    //Remove from local storage
    localStorage.removeItem('lastChannel');
}

//Redirects the user to the particular channel
function redirectToChannel(){
    var lastChannel = getLastChannel();
    //If last browsed channel exists, redirect
    if (lastChannel!=null) window.location = "/channel/"+lastChannel;
}

//Gets user display name
function getDisplayName(){
    //Gets from local storage
    var result = localStorage.getItem('displayName');
    //If data doesn't exists or invalid return null
    if (result == null) return null;
    else if (result.length <=0) return null;
    //Else return stored data
    else return result;
}

//Set new display name
function setDisplayName(displayName){
    //Save display name into the storage
    localStorage.setItem('displayName',displayName);
}

//Log out the user
function logout(){
    //Removes the display name from local storage
    localStorage.removeItem('displayName');
}

//Update the display name
function fixDisplayName(){
    //Define variables
    var displayname = document.querySelector('#displayname');
    var contents = document.querySelector('#contents');
    var login = document.querySelector('#loginform');
    //Get display name
    if (getDisplayName()!=null){//If display name exists
        displayname.innerHTML = getDisplayName();
        login.classList.add("hide");
        contents.classList.remove("hide");
    }
    else {//If user yet to login
        contents.classList.add("hide");
        login.classList.remove("hide");
    }
}

//Runs when onload
document.addEventListener('DOMContentLoaded', () => {
    //Submit username
    document.querySelector('#firstTimeForm').onsubmit = () => {
        //Set variables
        var inputname = document.querySelector('#dname').value;
        var loginmsg = document.querySelector('#loginmessage');
        //Check if empty
        if (inputname == '') loginmsg.innerHTML = "Field cannot be left empty! ";
        else {
            setDisplayName(inputname);
            fixDisplayName();
        }  
    }
    //Onclick logout
    document.querySelector('.logout').onclick = () => {
        logout();
        fixDisplayName();
    }

    //Run default functions on load
    fixDisplayName();
});
