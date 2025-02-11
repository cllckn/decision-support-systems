import time

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
    df = pd.read_csv("../../../../dataset/Employee.csv")

    for df_index, row in df.iterrows():
        employee_data = row.to_json()
        producer.produce(topic, key=str(df_index), value=employee_data, callback=delivery_report)
        print(employee_data)
        time.sleep(2)  # Introduce a 1-second delay between sending messages
    producer.flush() # If real-time message delivery is crucial, keep flush() inside the loop.
    # producer.flush() # If performance matters and a small delay is acceptable, move flush() outside the loop.
    print("All employee records sent successfully!")



# def produce_employee_data_as_stream():
#     """ Produces employee data records to a Kafka topic with a 1-second delay between messages. """
#     producer = Producer({'bootstrap.servers': kafka_config['bootstrap.servers']})  # Initialize Kafka producer
#
#     df = pd.read_csv("../../../../dataset/Employee.csv")  # Load dataset into a Pandas DataFrame
#
#     for _, row in df.iterrows():
#         employee_data = row.to_json()  # Convert row data to JSON format
#
#         producer.produce(
#             topic,
#             key=str(row['Age']),  # Use Age as the message key (optional)
#             value=employee_data,  # Send the employee record as a message
#             callback=delivery_report  # Attach callback function for delivery report
#         )
#
#         producer.flush()  # Ensure message is sent before proceeding
#         time.sleep(1)  # Introduce a 1-second delay between sending messages
#
#     print("All employee records sent successfully!")



if __name__ == "__main__":
    #produce_employee_data_as_stream()
    produce_employee_data()
