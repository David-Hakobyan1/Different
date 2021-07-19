from fbchat import log, Client
from fbchat.models import *
import credentials

class testBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        msgText=message_object.text
        msgText.lower()
        if msgText == 'hi' or msgText == "hello":
            self.send(Message(text="Hi my friend"), thread_id=thread_id,thread_type=thread_type )
        elif msgText == 'love':
            self.reactToMessage(message_object.uid, MessageReaction.LOVE)
        elif msgText == 'peace':
            self.reactToMessage(message_object.uid, MessageReaction.HEART)
            self.send(Message(text="First you must have peace in your heart, to give peace to anyone"), thread_id=thread_id, thread_type=thread_type )

client = testBot(credentials.email,credentials.password)
client.listen()
