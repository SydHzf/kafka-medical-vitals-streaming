from kafka import KafkaConsumer
import json
import time

print("Waiting for Kafka to start...")
time.sleep(20)

consumer = KafkaConsumer(
    "patient_vitals",
    bootstrap_servers='kafka:9092',
    api_version=(0,10),
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:

    data = message.value

    heart = data["heart_rate"]
    oxygen = data["oxygen"]

    if heart > 120:
        print("ALERT: Tachycardia detected", data)

    elif oxygen < 90:
        print("ALERT: Low Oxygen detected", data)

    else:
        print("Normal:", data)
