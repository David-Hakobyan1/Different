from fbchat import Client,log
from fbchat.models import*
import credentials
#from credentials import email,password

class Jarvis(Client):
    def onMessage(self,author_id=None,message_object=None,thread_id=None,thread_type=ThreadType.USER,**kwargs):
        self.markAsRead(author_id)
        log.info("message {} from {} in {}".format(message_object,thread_id,thread_type))
        msgText = message_object.text
        reply = "hello world"
        if author_id != self.uid:
            self.send(Message(text=reply),thread_id=thread_id,thread_type=thread_type)
        self.markAsDelivered(author_id,thread_id)
#client = Jarvis(email,password)
client = Jarvis(credentials.email,credentials.password)
client.listen()
