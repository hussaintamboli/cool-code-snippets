from amqplib import client_0_8 as amqp
import pdb
pdb.set_trace()
conn = amqp.Connection(host="localhost:5672 ", userid="celery_user",
                       password="celery_pass", virtual_host="/", insist=False)
chan = conn.channel()
name, jobs, consumers = chan.queue_declare(queue="delivery", passive=True)
print "name=%s jobs=%s consumers=%s" % (name, jobs, consumers)

