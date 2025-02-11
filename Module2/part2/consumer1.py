from confluent_kafka import Consumer, KafkaError

# Kafka broker configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address
    'group.id': 'my-group',                 # Consumer group ID
    'auto.offset.reset': 'earliest'         # Start reading from the beginning of the topic
}

# Create a Kafka consumer
consumer = Consumer(conf)

# Subscribe to the 'dss-test-topic1' topic
consumer.subscribe(['dss-test-topic1'])

# Poll for messages
try:
    while True:
        msg = consumer.poll(timeout=1.0)  # Wait for messages
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print(f"Reached end of partition {msg.partition()}")
            else:
                print(f"Error: {msg.error()}")
        else:
            # Print the message key and value
            print(f"Consumed: key={msg.key()}, value={msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    print("Consumer interrupted")
finally:
    # Close the consumer
    consumer.close()
