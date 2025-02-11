from confluent_kafka import Producer

# Kafka broker configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address
}

# Create a Kafka producer
producer = Producer(conf)


# Define a delivery callback to check if the message was successfully delivered
def delivery_callback(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


# Continuously read input from the terminal and send it to Kafka
def produce_messages():
    print("Kafka Producer is running. Type your messages and press Enter to send. Type 'exit' to quit.")
    while True:
        # Read input from the terminal
        message = input("Enter message: ")

        # Exit if the user types 'exit'
        if message.lower() == 'exit':
            print("Exiting producer...")
            break

        # Send the message to the 'dss-test-topic1' topic
        producer.produce(
            'dss-test-topic1',  # Topic name
            key=None,  # Message key (optional)
            value=message,  # Message value
            callback=delivery_callback
        )
        print(f"Produced: {message}")

        # Flush the producer to ensure the message is sent
        producer.flush()


if __name__ == "__main__":
    produce_messages()
