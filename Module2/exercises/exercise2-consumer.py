from confluent_kafka import Producer, Consumer, KafkaException
import pandas as pd
import json

topic = "dss-module2-exercise"
kafka_config = {
    'bootstrap.servers': 'localhost:9092',  # Update with actual Kafka broker address
    'group.id': 'employee-consumer-group',
    'auto.offset.reset': 'latest'
}

# Consumer

def consume_employee_data():
    consumer = Consumer(kafka_config)
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())

            #print(f"Received: key={msg.key()}, value={msg.value().decode('utf-8')}") #the byte object should be decoded using the UTF-8 encoding (a human-readable string.)
            print(f"Consumed: key={msg.key()}, value={msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        print("Consumer stopped.")
    finally:
        consumer.close()


if __name__ == "__main__":
    consume_employee_data()
