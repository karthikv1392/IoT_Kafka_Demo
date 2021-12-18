# IoT_Kafka_Demo
The demo of Apache Kafka given during Software Architecture Course for Masters students of the University of L'Aquila. 


## Commands to Get Started with Kafka

1. Download Apache Kafka - https://kafka.apache.org
2. Go inside the kafka root directory (using cd command)
3. Run bin/zookeeper-server-start.sh config/zookeeper.properties
4. Start the Kafka broker bin/kafka-server-start.sh config/server.properties
5. Create topic bin/kafka-topics.sh --create --topic sample1 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
6. Write to topics: bin/kafka-console-producer.sh --topic sample1 --broker-list localhost:9092
7. Consume from topics bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092


## Disclaimer

The above commands are written for Kafka 2.11. If you are using the latest version of Kafka, please refer to the following page: https://kafka.apache.org/quickstart


## For running the CupCarbon simulator and Kafka together

1. Download cupcarbon 5.0 from http://cupcarbon.com
2. Start the simulator by running the cupcarbon.jar file
3. From open projects browse to the folder IoT_Demo folder (found in this repo)
4. Select and load IoT_Demo.cup file as the project
5. Run the Python Kafka consumer first (python ThingsBoard_Consumer.py)
6. Start the simulation of the CupCarbon project using the play button found in the CupCarbon tool
7. Start the Python Kakfa producer (python Data_Producer.py)

