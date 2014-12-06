from kombu import Connection
from kombu import Queue
import json
import sys

userid, password, virtual_host, uri_prefix = 'celery_user', \
                  'celery_pass', 'delivery_reports', 'amqp://'
# or you could directly pass
# conn_settings = 'amqp://celery_user:celery_pass@localhost/delivery_reports'
# to the Connection()

if len(sys.argv) is 2:
    queue_name = sys.argv[1]
    with Connection(userid = userid, password = password, 
                virtual_host = virtual_host, 
                uri_prefix = uri_prefix) as conn:
	simple_queue = conn.SimpleQueue(queue_name)
        try:
	    message = simple_queue.get(block=True, timeout=1)
	    print("Received: %s" % json.loads(message.payload))
	    message.ack()
        except Exception, e:
            print("Queue %s empty" % queue_name)
	simple_queue.close()
        conn.release()
else:
    print 'Usage: %s <task_id>' % sys.argv[0]
