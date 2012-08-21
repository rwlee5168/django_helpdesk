# Create your views here.
from django.shortcuts import render_to_response
import boto.sns
import twilio.twiml
import re

"""
class Submission(colander.MappingSchema):
    firstname = colander.SchemaNode(colander.String())
 """
clients = {}
firstTimeclients = []


def home(request):
    # try:
    #     one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
    # except DBAPIError:
    #     return Response(conn_err_msg, content_type='text/plain', status_int=500)

    # return {}
    return render_to_response('mytemplate.html')


def done(request):
    sns = boto.sns.SNSConnection("AKIAIMRF4NLL75DXLOWA", "DtFZ9z5IAitkvMkMty8sy/KQ+1j5qmuCj9Lrow4Q")
    sns.publish("arn:aws:sns:us-east-1:820374392987:Wifi_help", "A user has requested help from the mobile help desk.")
    return render_to_response('done.html')


def twilio_response(request):
    global clients, firstTimeclients
    sns = boto.sns.SNSConnection("AKIAIMRF4NLL75DXLOWA", "DtFZ9z5IAitkvMkMty8sy/KQ+1j5qmuCj9Lrow4Q")
    text = re.sub(r'\W+', ' ', request.params['Body'])
    text_body = text.strip()
    text_from = request.params['From']
    body = text_body.split()
    containsNum = num_finder(text_body)
    try:
        if containsNum:
            if body[0].upper() == "REMOVE":
                subject = "+1" + str(body[1])
                clients.pop("+1" + str(body[1]))
                firstTimeclients.remove(subject)
                message2 = subject + " request has been fulfilled."
                message = message2
                sns.publish("arn:aws:sns:us-east-1:820374392987:Wifi_help", message2, "Wifi problem detected by " + subject)
            elif text_from not in firstTimeclients:
                firstTimeclients += [text_from]
                message2 = "Name: " + str(body[0]) + "\nLocation: " + list_str(body[1:])
                message = "Your message was received. If you need to change your room, text your new room number and building. E.g. \'325 Soda\' To cancel, text \'undo\'"
                sns.publish("arn:aws:sns:us-east-1:820374392987:Wifi_help", message2, "Wifi problem detected by " + text_from)
                clients[text_from] = text_body
            else:
                message = "The EECS Helpdesk has recieved your request and will send help to your updated room."
                message2 = str(clients[text_from].split()[0]) + " has changed location. \nNew location: " + text_body
                sns.publish("arn:aws:sns:us-east-1:820374392987:Wifi_help", message2, "Wifi problem detected by " + text_from)
                clients[text_from] = str(clients[text_from].split()[0]) + " " + text_body
        elif body[0].upper() == "WIFI":
            message = "The EECS Helpdesk got your message. Please respond with your first name, the room #, and building name on the poster. E.g. \'Joe 326 Soda\'"
            message2 = "A Wifi problem was detected, awaiting response."
            sns.publish("arn:aws:sns:us-east-1:820374392987:Wifi_help", message2, "Wifi problem detected by " + text_from)
        elif body[0].upper() == "RETRIEVE":
            hall_request = body[1].upper()
            message = ""
            message2 = "Current requests for " + hall_request + ":\n"
            for user in clients:
                if hall_request in clients[user].upper():
                    message = message + clients[user] + " "
                    message2 = message2 + clients[user] + "\n"
            if message == "":
                message = "none"
            sns.publish("arn:aws:sns:us-east-1:820374392987:Wifi_help", message2, "Help requests in " + hall_request)
        elif body[0].upper() == "UNDO":
            clients.pop(text_from)
            firstTimeclients.remove(text_from)
            message = "Your request had been received and cancelled"
            message2 = text_from + " cancelled request for assistance"
            sns.publish("arn:aws:sns:us-east-1:820374392987:Wifi_help", message2, "Wifi problem detected by " + text_from)
        else:
            message = "We are sorry, but we do not recognize this request"
    except:
        message = "We are sorry, but there was a problem with your request"

    resp = twilio.twiml.Response()
    resp.sms(message)

    return str(resp)


def num_finder(text):
    splitter = text.split()
    for element in splitter:
        if element.isdigit():
            return True
    return False


def list_str(lst):
    result = ""
    for element in lst:
        result = result + str(element) + " "
    return result
