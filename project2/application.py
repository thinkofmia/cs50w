import os

from flask import Flask, render_template, session, request, url_for
from flask_session import Session
from flask_socketio import SocketIO, emit
from datetime import datetime
import requests
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = True #Allows session to remain permanent even if browser is closed
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#Classes
class Message:
    def __init__(self, sender, content, timestamp):
        self.sender = sender
        self.content = content
        self.timestamp = timestamp

class Channel:
    def __init__(self, name):
        self.name = name
        self.messages = []
    def postMsg(self, message):
        self.messages.append(message)
        while len(self.messages) > 100:
            del(self.messages[0])
    def getMsg(self):
        return self.messages

#Create default channels
fakeChannel = Channel("demo1")
#Create default msg
botmsg = Message(sender="FlackBot", content="Hi! I am a bot. Let me guide you on your first channel. ", timestamp="Sun, 28 Jun 2020 07:17:05 GMT")
fakeChannel.postMsg(botmsg)

#Default Lists
channels = [fakeChannel] #List for channels
profiles = {"FlackBot":15} #List for profile pictures

#Routes
@app.route("/", methods=["GET","POST"])
def index(): #Home Page
        #Set Variables
        msg = "" #Var for error msg
        headline = "Channel List" #Var for headline
        #If post request/channel creation
        if request.method == "POST":
            #Get the channel name from the input box
            channelname = str(request.form.get('newchannel'))
            #Check if channel exists
            checkExists = False
            #Loop for all available channels
            for i in range(len(channels)):
                #If channel exists inside list return true
                if channels[i].name==channelname:
                    checkExists = True
            #If channel exists
            if (checkExists):
                #Display error msg
                msg = "Channel already exists! "
            else: #If channel doesnt exist, create a new channel with default settings
                newChannel = Channel(channelname)
                newChannel.postMsg(botmsg)
                channels.append(newChannel)
                msg = "Channel "+channelname+" added! "
        #Return template
        return render_template("channellist.html", headline=headline, channels=channels, msg=msg)

#Route for profile
@app.route("/profile")
def profile():
    headline = "Profile"
    return render_template("profile.html", headline=headline, profiles=json.dumps(profiles))

#Route for Channel
@app.route("/channel/<string:channelname>")
def viewchannel(channelname):  
    #Check if channel name exists
    checkExists = False
    index = 0
    #Loop for all available channels
    for i in range(len(channels)):
        #If channel name inside list return true
        if channels[i].name==channelname:
            checkExists = True
            index = i
    #If channel doesn't exist in list
    if (checkExists==False):
        #Return invalid page
        headline = "Invalid channel! "
        return render_template("index.html", headline=headline)
    else: #If channel exists return channel page
        return render_template("channel.html", headline=channelname, messages=channels[index].messages, profiles=json.dumps(profiles))        

#Sockets for real-time
#If socket is on posting a new message
@socketio.on("postMessage")
def post(data):
    #Set Variables
    channel = data['channel']
    sender = data['sender']
    content = data['content']
    timestamp = data['timestamp']
    #Create a new messsage class
    newmsg = Message(sender=sender, content=content, timestamp=timestamp)
    #Append msg to channel
    checkExists = False
    index = 0
    #Find which channel the user is sending from and if exists
    for i in range(len(channels)):
        if channels[i].name==channel:
            checkExists = True
            index = i
    #If channel exists
    if (checkExists):
        #Update the channel with the new message
        channels[index].postMsg(newmsg)
        #Update in real-time
        emit("updatePosts", data, broadcast=True)

#Update pictures in real-time
@socketio.on("changePic")
def changepic(data):
    #Set Variables
    choice = data['choice']
    user = data['user']
    #Update profile
    profiles[user] = choice
    #Emit the new profile data back to clients
    emit("updatePic", json.dumps(profiles), broadcast=True)

#When deleting messages in real-time
@socketio.on("deleteMessage")
def delete(data):
    #Set Variables
    channel = data['channel']
    sender = data['sender']
    timestamp = data['timestamp']
    #Check if channel exists
    checkExists = False
    index = 0
    #Loop for all channels in the list
    for i in range(len(channels)):
        #If channel is inside list, return true and get array index
        if channels[i].name==channel:
            checkExists = True
            index = i
    #If channel exists, delete msg
    if (checkExists):
        msg = channels[index].getMsg()
        #Loop for all messages and find the message
        for i in range(len(msg)):
            if (msg[i].sender == sender and msg[i].timestamp == timestamp):
                msg.pop(i)
                #Delete the message back in real-time
                emit("deletePost", data, broadcast=True)