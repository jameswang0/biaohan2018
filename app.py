from bottle import route, run, request, abort, static_file

from fsm import TocMachine

import os
ACCESS_TOKEN = 'EAAcLl8zZAaWABAKyZAEtCZAD893IsWRTSyCGHcOkd2KerM3LHMax5X2uDZBsPCOYlF30ZCF7NuWuMtXqPgSCK2qAqHZBdmrUO1fFDaZANh0oB2eRoGwpZCHru2EN7HQxDpBOPyq3dyJMiZByvopVhgZAouSUQgKyZC9h6lcZB06ZCX8LJeAZDZD'

VERIFY_TOKEN = '3345678'


#PORT = os.environ['PORT']

machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'state4',
        'test'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {   
            'trigger': 'advance',
            'source' : 'user',
            'dest': 'test',
            'conditions': 'is_going_to_test'
        },
        {
            'trigger': 'advance',
            'source': [
                'user',
                'state1'
            ],
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {   'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': [
                'state1',
                'state2'
            ],
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
                'state3',
                'state4',
                'test'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    #event = body['entry'][0]['messaging'][0]
    #global Records
    #sender_id = event['sender']['id']

    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="0.0.0.0", port=5000, debug=True, reloader=True)
