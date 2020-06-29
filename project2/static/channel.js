/**
 * channel.js
 * The JS file for the channel page
 */

var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

//Retrieve the last channel browsed
function getLastChannel(){
    //Get from local storage
    var result = localStorage.getItem('lastChannel');
    //If empty return null
    if (result == null) return null;
    //If invalid also return null
    else if (result.length <=0) return null;
    //Else return the stored string
    else return result;
}

//Remove or pop the last channel browsed from storage
function clearLastChannel(){
    //Remove from local storage
    localStorage.removeItem('lastChannel');
}

//Set the last channel browsed
function setLastChannel(channel){
    //Save the channel name into the local storage
    localStorage.setItem('lastChannel', channel);
}

//Does a check and update all the current posts
function checkAllPosts(){
    //Set array for all the posts
    var postArray = document.querySelectorAll('.post');
    //Loop for all posts
    for (var i=0;i<postArray.length;i++){
        var postSender = postArray[i].querySelector('.senderName').innerHTML;
        //If post belongs to user, display also the delete button
        if (postSender==getDisplayName()){
            showDeleteButton(postArray[i]);
            }
        }
}

//Deletes the post
function deletePost(elem){
    //Get parent node of the delete button
    var parent = elem.parentElement;
    //Get post information
    var timestamp = parent.querySelector('.timestamp').innerHTML;
    var sender = parent.querySelector('.senderName').innerHTML;
    var channel = getLastChannel();
    //Send to server
    socket.emit('deleteMessage', {"channel": channel, "sender": sender, "timestamp": timestamp});
}

//Displays the delete button
function showDeleteButton(element){
    //Add button
    var deleteButton = document.createElement("span");
    deleteButton.className = "deleteButton";
    deleteButton.innerHTML = "x";
    deleteButton.addEventListener("click", function(event) {
        deletePost(event.target);
    });
    //Append to post
    element.appendChild(deleteButton);
}

//Posts the message to the server
function sendMessage(channel, sender, content, timestamp){
    //Send the message in real time
    socket.emit('postMessage', {"channel": channel, "sender": sender, "content": content, "timestamp": timestamp});
}

//Scroll the div to the bottom
function scrollToLatest(){
    var display = document.querySelector('#posts');
    //If the display for the posts is visible
    if (display.className != "hide") display.scrollTop = display.scrollHeight;
}

//Update profile pic for all the posts
function updateAllPics(){
    //Get the json data of the profile pics
    var data = document.querySelector('#profilesdata').innerHTML;
    data_array = JSON.parse(data);
    //Loop for each profile in data
    for (var name in data_array){
        //console.log("key = "+ name+" value = "+data_array[name]);
        //Update the picture of the post
        updatePic(name, data_array[name]);
    }
}

//Get the profile pic of the user
function getPic(user){
    //Get the json data of the profile pic
    var data = document.querySelector('#profilesdata').innerHTML;
    data_array = JSON.parse(data);
    //Loop for each profile in data
    for (var name in data_array){
        //If user matches the name in the profile
        if (name==user){
            //Returns the pic selected
            return data_array[name];
        }
    }
    //Else just return the default 1
    return 1;
}

//Update the profile pic of the user
function updatePic(user, pic){
    var sender = document.querySelectorAll('.senderName');
    //Loop for all sender posts
    for (var i=0;i<sender.length;i++){
        //If the sender is the user selectd
        if (sender[i].innerHTML==user){
            //Update the src of the image
            var parent = sender[i].parentElement;
            var picture = parent.querySelector('.displaypic');
            picture.src = "/static/images/"+pic+".jpg";
        }
    }
}

//Runs when onload
document.addEventListener('DOMContentLoaded', () => {
    //Send Message
    document.querySelector('#sendmsg').onclick = () => {
        //Get contents, channel and sender name
        var contents = document.querySelector('#newmsg').value;
        var user = getDisplayName();
        var channel = getLastChannel();
        //Get Date-Time
        var dt = new Date();
        var utcDate = dt.toUTCString();
        var timestamp = utcDate;
        if (contents.length>0) sendMessage(channel, user, contents, timestamp);
        //Clear input field
        document.querySelector('#newmsg').value = "";
    }

    // Execute a function when the user releases a key on the keyboard
    document.querySelector('#newmsg').addEventListener("keyup", function(event) {
    // Number 13 is the "Enter" key on the keyboard
    if (event.keyCode === 13) {
        // Cancel the default action, if needed
        event.preventDefault();
        // Trigger the button element with a click
        document.querySelector('#sendmsg').click();
    }
    }); 

    
    //Successful deletion real time
    socket.on('deletePost', data => {
        //Set var
        var postsArray = document.querySelectorAll('.post');
        var timestamp = data['timestamp'];
        var sender = data['sender'];
        var channel = data['channel'];
        //Check if correct channel
        if (channel == getLastChannel()){
            //Loop all the available posts
            for (var i=0;i<postsArray.length;i++){
                //Get respective elements
                var postTime = postsArray[i].querySelector('.timestamp').innerHTML;
                var postSender = postsArray[i].querySelector('.senderName').innerHTML;
                //Check if exists
                if (timestamp == postTime && sender == postSender){
                    //Hide the post
                    postsArray[i].style.display = "none";
                }
            }
        }
    });

    //Update channel real time
    socket.on('updatePosts', data => {
        //Set var
        var display = document.querySelector('#posts');
        var timestamp = data['timestamp'];
        var sender = data['sender'];
        var contents = data['content'];
        var channel = data['channel'];
        //Check if correct channel
        if (channel == getLastChannel()){
            //Create post div
            post = document.createElement("div");
            post.id = timestamp+sender;
            post.className = "post";
            //Add img
            newimg = document.createElement("img");
            newimg.className = "displaypic";
            newimg.src = "/static/images/"+getPic(sender)+".jpg";
            post.appendChild(newimg);
            //Add timestamp
            newtimestamp = document.createElement("span");
            newtimestamp.className = "timestamp";
            newtimestamp.innerHTML = timestamp;
            post.appendChild(newtimestamp);
            //Add sender
            newsender = document.createElement("span");
            newsender.className = "senderName";
            newsender.innerHTML = sender;
            post.appendChild(newsender);
            //Add contents
            post.innerHTML += ": "+contents;
            //Append post to display
            display.appendChild(post);
            //Scroll to latest post
            scrollToLatest();
            //Update posts with pic
            updateAllPics();
            if (sender==getDisplayName())showDeleteButton(post);
        }
    });

    //Update pics
    socket.on('updatePic', data => {
        //Update json data of the profile pics
        var pictures = document.querySelector('#profilesdata');
        pictures.innerHTML = data;
        console.log(data);
        //Update all posts with the new pics
        updateAllPics();
    });
    //Run default functions on load
    checkAllPosts();
    updateAllPics();
    scrollToLatest();
});
