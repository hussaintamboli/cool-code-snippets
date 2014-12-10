from kombu import Connection, Producer, Queue
from kombu import common
from kombu.message import Message
from kombu.simple import SimpleQueue
import uuid
import json

userid, password, virtual_host, uri_prefix = 'celery_user', \
                  'celery_pass', 'delivery_reports', 'amqp://'
# or you could directly pass
# conn_settings = 'amqp://celery_user:celery_pass@localhost/delivery_reports'
# to the Connection()

queue_name, exchange, routing_key = 'celery', 'celery', 'celery'
task_id, task_name = str(common.uuid()), 'CeleryWorker.PushToSalesforce'

data = {
    "smsId" : "3568084",
    "status" : "DELIVERED",
    "externalId" : "00590000002lBajAAE-451506f12265",
    "accountId" : "80001837",
    "sentStatus" : "success",
    "responseId" : "00590000002lBajAAE-ef5dd6b1edd5"
}
payload = {
    "id" : task_id,
    "task" : task_name,
    "args" : [data],
    "retries" : 0
}
payload = json.dumps(payload)  #json payload

with Connection(userid = userid, password = password, 
                virtual_host = virtual_host, 
                uri_prefix = uri_prefix) as conn:
    channel = conn.channel()
    queue = Queue(queue_name, exchange = exchange, routing_key = routing_key)
    #message = Message(channel, body = payload)
    producer = Producer(conn)
    #message = Message(jsonpayload)
    producer.publish(payload, routing_key = routing_key, exchange = exchange, 
                     correlation_id = task_id, reply_to = queue_name)
    #simple_queue = conn.SimpleQueue(queue_name)
    #simple_queue.put(message)
    print('sending task with task_id=%s having payload=%s' % (task_id, payload))
    #simple_queue.close()
    channel.close()
    conn.release()

