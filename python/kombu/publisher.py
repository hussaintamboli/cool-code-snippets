from kombu import Connection
import uuid
import json

userid, password, virtual_host, uri_prefix = 'celery_user', \
                  'celery_pass', 'delivery_reports', 'amqp://'
# or you could directly pass
# conn_settings = 'amqp://celery_user:celery_pass@localhost/delivery_reports'
# to the Connection()

queue_name, exchange, routing_key = 'celery', 'celery', 'celery'
task_id, task_name = str(uuid.uuid1()), 'CeleryWorker.PushToSalesforce'
payload = {
    "smsId":"3568084",
    "status":"DELIVERED",
    "externalId":"00590000002lBajAAE-451506f12265",
    "accountId":"80001837",
    "sentStatus":"success",
    "responseId":"00590000002lBajAAE-ef5dd6b1edd5"
}
message = json.dumps(payload)  #json payload

with Connection(userid = userid, password = password, 
                virtual_host = virtual_host, 
                uri_prefix = uri_prefix) as conn:
    simple_queue = conn.SimpleQueue(queue_name)
    simple_queue.put(message)
    print('sending task with task_id=%s having payload=%s' % (queue_name, message))
    simple_queue.close()
    conn.release()

