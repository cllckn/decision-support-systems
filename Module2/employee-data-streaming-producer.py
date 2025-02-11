import time

from confluent_kafka import Producer, Consumer, KafkaException
import pandas as pd
import json
from io import StringIO


topic = "dss-employee-parallel-processing"
kafka_config = {
    'bootstrap.servers': 'localhost:9092',  # Update with actual Kafka broker address

}


# Producer

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] with key {msg.key().decode('utf-8')}")


def produce_employee_data_as_stream():
    producer = Producer({'bootstrap.servers': kafka_config['bootstrap.servers']})

    with open("../../../dataset/Employee.csv", "r") as file:
        header = next(file)  # Read the header row
        for index, line in enumerate(file):  # Read line by line
            row = pd.read_csv(StringIO(header + line))  # Convert line to DataFrame
            employee_data = row.iloc[0].to_json()  # Convert first row to JSON

            print(f"Preparing to send record {index}: {employee_data}")  # Print before sending

            producer.produce(topic, key=str(index), value=employee_data, callback=delivery_report)

            producer.flush()  # Ensure message is sent before processing the next line

            time.sleep(1)  # Add a 1-second delay before reading the next record

    print("All employee records sent successfully!")

if __name__ == "__main__":
    produce_employee_data_as_stream()
    # produce_employee_data()
