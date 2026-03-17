# Real-Time Medical Simulation Monitoring System using Apache Kafka

## 📌 Overview

This project demonstrates a real-time data streaming pipeline for medical simulation using Apache Kafka. It simulates patient vital signs such as heart rate and oxygen levels, processes them in real time, and detects abnormal conditions.

The system is fully containerized using Docker, ensuring a consistent and reproducible environment.

---

## ⚙️ Technologies Used

* Apache Kafka
* Docker & Docker Compose
* Python (kafka-python)
* Zookeeper

---

## 🏗️ System Architecture

Medical Simulator (Producer)
→ Kafka Topic (`patient_vitals`)
→ Consumer (Processing & Alerts)

---

## 🚀 Features

* Real-time simulation of patient vital data
* Event-driven streaming using Kafka
* Detection of abnormal conditions:

  * High heart rate (Tachycardia)
  * Low oxygen level (Hypoxia)
* Containerized setup using Docker

---

## 📂 Project Structure

```
medical-kafka-simulation/
│
├── docker-compose.yml
├── producer/
│   ├── Dockerfile
│   └── producer.py
├── consumer/
│   ├── Dockerfile
│   └── consumer.py
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone <your-repo-url>
cd medical-kafka-simulation
```

### 2. Start the system

```
docker compose up --build
```

### 3. Observe output

* Producer sends simulated patient data
* Consumer processes data and prints alerts

---

## 📊 Example Output

```
Sent: {'heart_rate': 130, 'oxygen': 95}
ALERT: Tachycardia detected
```

---

## 🧠 Learning Outcomes

* Understanding real-time data streaming
* Working with Kafka producers and consumers
* Event-driven architecture
* Containerized workflows using Docker

---

## 🔮 Future Improvements

* Add real-time dashboard (Grafana / Streamlit)
* Store data in database (PostgreSQL / MongoDB)
* Simulate multiple patients
* Implement advanced analytics

---

## 📌 Author

Syed Huzaifa Ali
