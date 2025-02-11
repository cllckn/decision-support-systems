from datetime import datetime

from confluent_kafka import Producer, Consumer, KafkaException
import pandas as pd
import json

topic = "dss-module2-exercise"
kafka_config = {
    'bootstrap.servers': 'localhost:9092',  # Update with actual Kafka broker address
    'group.id': 'employee-consumer-group',
    'auto.offset.reset': 'latest'
}


def process_data(json_string):
    try:
        # 1 Data Parsing: Parse JSON input
        data = json.loads(json_string)

        # 2 Data Validation: type checking types and limits of values
        required_fields = ["Age", "Gender", "Education", "JoiningYear", "ExperienceInCurrentDomain", "LeaveOrNot",
                           "EverBenched"]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        if not isinstance(data["Age"], int) or not (18 <= data["Age"] <= 65):
            raise ValueError("Invalid Age: Must be an integer between 18 and 65")
        # 2 Data Cleaning: Standardizing text fields (case normalization, trimming spaces)
        data["Education"] = data["Education"].strip().lower()       # trim space and trim spaces and normalize case (
        # converts all characters to lowercase )
        data["City"] = data["City"].strip().title()  # trim spaces, capitalizes the first letter of each word
        data["Gender"] = data["Gender"].strip().capitalize()  # trim spaces and converts the
        # first letter to uppercase and the rest to lowercase
        data["EverBenched"] = 1 if data["EverBenched"].strip().lower() == "yes" else 0

        # 3 Feature Engineering: Compute "YearsSinceJoining"
        current_year = datetime.now().year
        data["YearsSinceJoining"] = current_year - data["JoiningYear"]

        # 4 Encoding: Convert categorical values to numbers
        education_mapping = {"bachelors": 1, "masters": 2, "phd": 3}
        data["Education"] = education_mapping.get(data["Education"], 0)  # default 0

        gender_mapping = {"Male": 0, "Female": 1}
        data["Gender"] = gender_mapping.get(data["Gender"], -1)  # default -1

        # 5 Business Logic: Identify high-risk employees
        data["HighRiskEmployee"] = 1 if (
                data["ExperienceInCurrentDomain"] < 2 and data["Age"] < 30 and data["LeaveOrNot"] == 1
        ) else 0

        # 6 Data Validation: Ensure logical consistency
        if data["ExperienceInCurrentDomain"] > data["YearsSinceJoining"]:
            raise ValueError("Invalid Data: Experience exceeds years since joining")

        return json.dumps(data, indent=4)  # Convert the Python dictionary (data) into a JSON-formatted string. indent=4 makes the JSON more human-readable(pretty)

    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON format"})
    except ValueError as e:
        return json.dumps({"error": str(e)})


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
            # Decode and process the message
            decoded_value = msg.value().decode('utf-8')
            processed_value = process_data(decoded_value)

            print(f"Consumed: key={msg.key()}, processed_value={processed_value}")

    except KeyboardInterrupt:
        print("Consumer stopped.")
    finally:
        consumer.close()


if __name__ == "__main__":
    consume_employee_data()
