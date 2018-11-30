from kafka import KafkaProducer
import sys

if __name__ == "__main__":
    # 步驟1.設定要連線到Kafka集群的相關設定, 並產生一個Kafka的Producer的實例
    producer = KafkaProducer(
        # Kafka集群在那裡?
        bootstrap_servers=["localhost:9092"],
        # 指定msgKey的序列化器, 若Key為None, 無法序列化, 透過producer直接給值
        # key_serializer=str.encode,
        # 指定msgValue的序列化器
        value_serializer=str.encode
    )

    # 步驟2.指定想要發佈訊息的topic名稱
    topic_name = "testTopic2"

    msg_counter = 0
    try:
        print("Start sending messages ...")
        # 步驟3.產生要發佈到Kafka的訊息
        # - 參數  # 1: topicName
        # - 參數  # 2: msgKey
        # - 參數  # 3: msgValue
        producer.send(topic=topic_name, key=None, value="Hello")
        producer.send(topic=topic_name, key=None, value="Hello2")
        producer.send(topic=topic_name, key=b"sgxxxx", value='Hello3')
        producer.send(topic=topic_name, key=b"sgxxxx", value="Hello4")
        msg_counter += 4
        print("Send " + str(msg_counter) + " messages to Kafka")
        print("Message sending completed!")
    except Exception as e:
        # 錯誤處理
        e_type, e_value, e_traceback = sys.exc_info()
        print("type ==> %s" % (e_type))
        print("value ==> %s" % (e_value))
        print("traceback ==> file name: %s" % (e_traceback.tb_frame.f_code.co_filename))
        print("traceback ==> line no: %s" % (e_traceback.tb_lineno))
        print("traceback ==> function name: %s" % (e_traceback.tb_frame.f_code.co_name))
    finally:
        # 步驟4.關掉Producer實例的連線
        producer.close()
