# Setting Up the Development Environment

## APACHE KAFKA

    Download Apache Kafka and extract it
        https://kafka.apache.org/downloads
        Binary downloads:
        Scala 2.12  - kafka_2.12-3.5.0.tgz (asc, sha512)
        Scala 2.13  - kafka_2.13-3.5.0.tgz (asc, sha512)
        Extract the downloaded file
        Open a Terminal/Console to run each of the following binary files.
  ~~~bash
  cd .../kafka/bin
  sh zookeeper-server-start.sh ../config/zookeeper.properties 
  sh kafka-server-start.sh ../config/server.properties
  
  
  # topic operations
  ./kafka-topics.sh -list --bootstrap-server localhost:9092
  ./kafka-topics.sh -create --bootstrap-server localhost:9092 --topic dss-test-topic1
  
  
  # producer&consumer
  ./kafka-console-producer.sh --bootstrap-server localhost:9092 --topic --topic dss-test-topic1
  ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic --topic dss-test-topic1
  ~~~

**Running .sh files on Windows can be challenging. You may need to install Git Bash.**

