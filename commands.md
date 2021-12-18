## Commands to Get Started with Kafka

1. Download Apache Kafka
2. Run bin/zookeeper-server-start.sh config/zookeeper.properties
3. Start the Kafka broker bin/kafka-server-start.sh config/server.properties
4. Create topic bin/kafka-topics.sh --create --topic sample1 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
4. Write to topics: bin/kafka-console-producer.sh --topic sample1 --broker-list localhost:9092
5. Consume from topics bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092


## Disclaimer

The above commands are written for Kafka 2.11. If you are using the latest version of Kafka, please refer to the following page: https://kafka.apache.org/quickstart


## Change JAVA to the orignal version

export JAVA_HOME=`/usr/libexec/java_home -v 1.8`