from kafka import KafkaProducer
import json
import time
import random

print("Waiting for Kafka to start...")
time.sleep(20)
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    api_version=(0,10),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

patient_id = "SIM001"

while True:

    data = {
        "patient_id": patient_id,
        "heart_rate": random.randint(60,140),
        "oxygen": random.randint(85,100),
        "timestamp": time.time()
    }

    producer.send("patient_vitals", data)

    print("Sent:", data)

    time.sleep(2)
