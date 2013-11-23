import logging

from sleekxmpp import ClientXMPP

SERVER = 'gcm.googleapis.com'
PORT = 5235
USERNAME = "512994705229@gcm.googleapis.com"
API_KEY = "AIzaSyA729Zb6trwUUulzMKWUpVhel5Yrg88ihs"


class OCDClient(ClientXMPP):

    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)
        self.add_event_handler("session_start", self.start)
        self.add_event_handler('message', self.receive_message)

        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0199') # XMPP Ping

    def start(self, event):
        self.send_presence()
        self.get_roster()

    def receive_message(self, message):
        if message['type'] in ('chat', 'normal'):
            print "message received"
            print message

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)-8s %(message)s')
    xmpp = OCDClient(USERNAME, API_KEY)
    if xmpp.connect(address=(SERVER, PORT)):
        xmpp.process(block=False)
        print "listening"
    else:
        print "can't connect"
