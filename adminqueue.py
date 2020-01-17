from twilio.rest import Client

class Adminqueue:

    def __init__(self):
        self.account_sid = 'AC525fc0164447c37a25351609991853f2'
        self.auth_token = '8b519937bc23d24b2dcc2311701cba9b'
        self.client = Client(self.account_sid, self.auth_token)
        self._queue = []
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = 'FIFO'

    def enqueue(self, item):
        self._queue.append(item)
        message = self.client.messages.create(
                              body='Welcome,' + str(item['name']) + ' You will be attended after of' + str(self.size()) + 'persons!!',
                              from_='+15085031878',
                              to = str(item['phone'])
                          )
        return message.sid

    def dequeue(self):
        if self.size() > 0:
            if self._mode == 'FIFO':
                item = self._queue.pop()
                return item
            elif self._mode == 'LIFO':
                item = self._queue.pop(-1)
                return item
        else:
            msg = {
                "msg": "Fila sin elementos"
            }
            return msg

    def get_queue(self):
        return self._queue


    def size(self):
        return len(self._queue) 

