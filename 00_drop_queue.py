#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()
channel.queue_delete(queue='reindex')
connection.close()
