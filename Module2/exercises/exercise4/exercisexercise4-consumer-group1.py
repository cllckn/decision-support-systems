from datetime import datetime
from confluent_kafka import Producer, Consumer, KafkaException
import pandas as pd
import json

topic = "dss-employee-parallel-processing"
processed_topic = "dss-employee-processed"

kafka_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'employee-consumer-group',
    'auto.offset.reset': 'latest'
}

producer = Producer({'bootstrap.servers': kafka_config['bootstrap.servers']})


def process_data(json_string):
    try:
        # 1. Data Parsing
        data = json.loads(json_string)

        # 2. Data Validation
        required_fields = ["Age", "Gender", "Education", "JoiningYear", "ExperienceInCurrentDomain", "LeaveOrNot", "EverBenched"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        if not isinstance(data["Age"], int) or not (18 <= data["Age"] <= 65):
            raise ValueError("Invalid Age: Must be an integer between 18 and 65")

        if not isinstance(data["JoiningYear"], int) or data["JoiningYear"] > datetime.now().year:
            raise ValueError("Invalid JoiningYear: Must be a valid past year")

        if not isinstance(data["ExperienceInCurrentDomain"], int) or data["ExperienceInCurrentDomain"] < 0:
            raise ValueError("Invalid Experience: Must be a non-negative integer")

        if not isinstance(data["LeaveOrNot"], int) or data["LeaveOrNot"] not in [0, 1]:
            raise ValueError("Invalid LeaveOrNot: Must be 0 or 1")

        if not isinstance(data["EverBenched"], str) or data["EverBenched"].strip().lower() not in ["yes", "no"]:
            raise ValueError("Invalid EverBenched: Must be 'Yes' or 'No'")

        # 3. Data Cleaning
        data["Education"] = data["Education"].strip().lower()
        data["City"] = data["City"].strip().title()
        data["Gender"] = data["Gender"].strip().capitalize()
        data["EverBenched"] = 1 if data["EverBenched"].strip().lower() == "yes" else 0

        # 4. Feature Engineering
        current_year = datetime.now().year
        data["YearsSinceJoining"] = current_year - data["JoiningYear"]

        # 5. Encoding
        education_mapping = {"bachelors": 1, "masters": 2, "phd": 3}
        data["Education"] = education_mapping.get(data["Education"], 0)

        gender_mapping = {"Male": 0, "Female": 1}
        data["Gender"] = gender_mapping.get(data["Gender"], -1)

        # 6. Business Logic
        data["HighRiskEmployee"] = 1 if (data["ExperienceInCurrentDomain"] < 2 and data["Age"] < 30 and data["LeaveOrNot"] == 1) else 0

        # 7. Data Validation
        if data["ExperienceInCurrentDomain"] > data["YearsSinceJoining"]:
            raise ValueError("Invalid Data: Experience exceeds years since joining")

        return json.dumps(data, indent=4)

    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON format"})
    except ValueError as e:
        return json.dumps({"error": str(e)})


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

            decoded_value = msg.value().decode('utf-8')
            processed_value = process_data(decoded_value)

            print(f"Consumed: key={msg.key()}, processed_value={processed_value}")

            # Convert processed_value back to a Python dictionary for filtering
            processed_data = json.loads(processed_value)

            # If Gender == 1, send to "dss-employee-processed" topic
            if processed_data.get("Gender") == 1:
                print(f"Forwarding to {processed_topic}: {processed_value}")
                producer.produce(processed_topic, key=msg.key(), value=processed_value)
                producer.flush()

    except KeyboardInterrupt:
        print("Consumer stopped.")
    finally:
        consumer.close()


if __name__ == "__main__":
    consume_employee_data()
