from google.cloud import bigquery
from google.cloud import storage ,streaming,bigtable

from google.cloud import pubsub

# Instantiates a client
pubsub_client = pubsub.Client()


topic_lists = pubsub_client.list_topics();

topics = topic_lists[0]
for topic in topics :
     print(topic.name)


# The name for the new topic
topic_name = 'my-new-topic3'

# Prepares the new topic
topic = pubsub_client.topic(topic_name)

# Creates the new topic
#topic.create()

print('Topic {} created.'.format(topic.name))