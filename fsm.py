import os
parendir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parendir)


import json
import requests
from transitions.extensions import GraphMachine
from utils import send_text_message
from fbmq import Attachment, Template, QuickReply, NotificationType


ACCESS_TOKEN = 'EAAcLl8zZAaWABAKyZAEtCZAD893IsWRTSyCGHcOkd2KerM3LHMax5X2uDZBsPCOYlF30ZCF7NuWuMtXqPgSCK2qAqHZBdmrUO1fFDaZANh0oB2eRoGwpZCHru2EN7HQxDpBOPyq3dyJMiZByvopVhgZAouSUQgKyZC9h6lcZB06ZCX8LJeAZDZD'

VERIFY_TOKEN = '3345678'

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        # self.fb_id = fb_id
        self.machine = GraphMachine(
                model=self,
                **machine_configs
        )
    '''
    def text_message(self, content):
        response_msg = json.dumps({"recipient": {"id": self.fb_id}, "message": {"text": content}})
        requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)

    def image_message(self, image):
        response_img = json.dumps({"recipient": {"id": self.fb_id}, "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": image
                }
            }
        }
                                   })
        requests.post(post_message_url, headers={"Content-Type": "application/json"},
                      data=response_img)

    def template_message(self, title, image_url, subtitle, data):
        response_template = json.dumps({"recipient": {"id": self.fb_id}, "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": title,
                            "image_url": image_url,
                            "subtitle": subtitle,
                            "buttons": data
                        }
                    ]
                }
            }
        }
                                        })
        requests.post(post_message_url, headers={"Content-Type": "application/json"},
                      data=response_template)

    def quick_reply_message(self, text, quick_replies):
        response_fast = json.dumps({"recipient": {"id": self.fb_id}, "message": {
            "text": text,
            "quick_replies": quick_replies
        }})
        requests.post(post_message_url, headers={"Content-Type": "application/json"},
                      data=response_fast)
        
'''

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state1'
        return False
    def is_going_to_test(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to test'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state2'
        return False
    
    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state3'
        return False
    
    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state4'
        return False


    def on_enter_state1(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "進入state1")
        self.go_back()
   

    def on_exit_state1(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "leaving state 1")
        print('Leaving state1')
        
    def on_enter_test(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "進入test")
        self.go_back()
   

    def on_exit_test(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "leaving test")
        print('Leaving test')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state2")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')
    
    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state3")
        self.go_back()

    def on_exit_state3(self):
        print('Leaving state3')

    def on_enter_state4(self, event):
        print("I'm entering state4")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state4")
        self.go_back()

    def on_exit_state4(self):
        print('Leaving state4')
    

