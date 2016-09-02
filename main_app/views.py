import json, requests, random, re
from pprint import pprint
import json
from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

#url = 'http://api.wordnik.com:80/v4/word.json/tycoon/definitions?limit=200&includeRelated=true&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'
def get_meaning(fbid, recieved_message):
	url = 'http://api.wordnik.com:80/v4/word.json/' + recieved_message + '/definitions?limit=200&includeRelated=true&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'
	r = requests.get(url)
	data = json.loads(r.text)
	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'% access_token
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":data}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())




class dictbot(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == verify_token:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)
 
 
    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']: 
                if 'message' in message: 
                    try:  
                        get_meaning(message['sender']['id'], message['message']['text'])
                    except Exception as e:
                        print e
                        get_meaning(message['sender']['id'], 'Please send a valid text.')    
        return HttpResponse()