# Project 2: Flack
Web Programming with Python and JavaScript

## Objectives
- Learn to use JavaScript to run code server-side.
- Become more comfortable with building web user interfaces.
- Gain experience with Socket.IO to communicate between clients and servers.

## Overview
In this project, we build an online messaging service using Flask, similar in spirit to Slack. Users will be able to sign into the site with a display name, create channels (i.e. chatrooms) to communicate in, as well as see and join existing channels. Once a channel is selected, users will be able to send and receive messages with one another in real time. 

Youtube Link: https://youtu.be/79SxC7fJfQY

## Files
- 'application.py' is the main app that runs the entire server. It also stores the necessary information for messages and profile pics on the server side

In the folder static
- Folder 'images' contains all the images a user can use for their profile pic
- 'flackChat.js' is the main js file to store the local session of a user (to remember their username and last browsed channel)
- 'channel.js' is the js file for all the javascript functions used while viewing a particular channel
- 'profile.js' is the js file for all js functions used to change a user's profile pic
- 'template.scss' and 'template.css' are the main css files used for all the html pages

In the folder templates
- 'index.html' is the default and base html display to be showed
- 'channel.html' is the html display for a particular channel which shows all of its messages
- 'channellist.html' is the html display for all the available channels to be browsed
- 'profile.html' is the html display for the user profile, allowing them to change their profile pic

## Personal Touch / Bonus Features
1. Set your own display picture
    The users are able set their own display pictures from the 16 images available. They also update the users in real-time upon image changes in any channel.

2. Delete your own messages
    Users are also able to delete their own messages if it doesn't look pleasant for them.

## Requirements
[x] Display Name: When a user visits your web application for the first time, they should be prompted to type in a display name that will eventually be associated with every message the user sends. If a user closes the page and returns to your app later, the display name should still be remembered.

[x] Channel Creation: Any user should be able to create a new channel, so long as its name doesn’t conflict with the name of an existing channel.

[x] Channel List: Users should be able to see a list of all current channels, and selecting one should allow the user to view the channel. We leave it to you to decide how to display such a list.

[x] Messages View: Once a channel is selected, the user should see any messages that have already been sent in that channel, up to a maximum of 100 messages. Your app should only store the 100 most recent messages per channel in server-side memory.

[x] Sending Messages: Once in a channel, users should be able to send text messages to others the channel. When a user sends a message, their display name and the timestamp of the message should be associated with the message. All users in the channel should then see the new message (with display name and timestamp) appear on their channel page. Sending and receiving messages should NOT require reloading the page.

[x] Remembering the Channel: If a user is on a channel page, closes the web browser window, and goes back to your web application, your application should remember what channel the user was on previously and take the user back to that channel.

[x] Personal Touch: Add at least one additional feature to your chat application of your choosing! Feel free to be creative, but if you’re looking for ideas, possibilities include: supporting deleting one’s own messages, supporting use attachments (file uploads) as messages, or supporting private messaging between two users.

[x] In README.md, include a short writeup describing your project, what’s contained in each file, and (optionally) any other additional information the staff should know about your project. Also, include a description of your personal touch and what you chose to add to the project.

[x] If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to requirements.txt!
