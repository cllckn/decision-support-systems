# Setting Up the Development Environment

## PyCharm

* Install Python
* Install PyCharm Professional

## APACHE KAFKA

Download Apache Kafka and extract it

    https://kafka.apache.org/downloads
    Binary downloads:
        Scala 2.13  - kafka_2.13-3.5.0.tgz (asc, sha512)
    Extract the downloaded file
    
    
Run each of the following binary files in a new terminal/console window.

~~~bash
# For Linux, OSX

cd .../kafka/bin

# Initialize apache Kafka Cluster
sh zookeeper-server-start.sh ../config/zookeeper.properties
sh kafka-server-start.sh ../config/server.properties


# topic operations
./kafka-topics.sh -create --bootstrap-server localhost:9092 --topic dss-test-topic1
./kafka-topics.sh -list --bootstrap-server localhost:9092

# producer & consumer
./kafka-console-producer.sh --bootstrap-server localhost:9092 --topic dss-test-topic1
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic dss-test-topic1
~~~

~~~bash
# For Windows

cd c:\.....\kafka\bin

# Initialize apache Kafka Cluster
.\zookeeper-server-start.bat ..\..\config\zookeeper.properties
.\kafka-server-start.bat  ..\..\config\server.properties

# topic operations
.\kafka-topics.bat --create  --topic dss-test-topic1 --bootstrap-server localhost:9092
.\kafka-topics.bat --list --bootstrap-server localhost:9092

# producer & consumer
 .\kafka-console-producer.bat --bootstrap-server localhost:9092 --topic dss-test-topic1
 .\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic dss-test-topic1
~~~


