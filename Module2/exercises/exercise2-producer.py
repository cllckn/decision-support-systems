from confluent_kafka import Producer
import pandas as pd
import json

topic = "dss-module2-exercise"
kafka_config = {
    'bootstrap.servers': 'localhost:9092',  # Update with actual Kafka broker address

}


# Producer

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


def produce_employee_data():
    producer = Producer({'bootstrap.servers': kafka_config['bootstrap.servers']})
    df = pd.read_csv("../../../dataset/Employee.csv")

    for _, row in df.iterrows():
        employee_data = row.to_json()
        producer.produce(topic, key=str(row['Age']), value=employee_data, callback=delivery_report)
        producer.flush()
    print("All employee records sent successfully!")


if __name__ == "__main__":
    produce_employee_data()
