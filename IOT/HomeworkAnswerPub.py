from kafka import KafkaProducer
import sys

KAFKA_BROKER_URL = "localhost:9092" # 設定要連接的Kafka群
WORKSHOP_ID = "01"
STUDENT_ID = "sgxxxx" # ** * < -- 修改成你 / 妳的學生編號

if __name__ == "__main__":
    # 步驟1.設定要連線到Kafka集群的相關設定, 並產生一個Kafka的Producer的實例
    producer=KafkaProducer(
        # Kafka集群在那裡?
        bootstrap_servers=["localhost:9092"],
        # 指定msgKey的序列化器, 若Key為None, 無法序列化, 透過producer直接給值
        key_serializer=str.encode,
        # 指定msgValue的序列化器
        value_serializer=str.encode
    )
    # 步驟2. 指定想要發佈訊息的topic名稱
    topic_name = "ak01.ws" + WORKSHOP_ID + ".homework"  # 個人作業繳交的Topic

    msgCounter = 20; # ak01的作業總共有20題
    try:
        print("Start sending messages ...")
         # 步驟3.產生要發佈到Kafka的訊息(把訊息封裝進一個ProducerRecord的實例中)
         # - 參數  # 1: topicName, 參數#2: msgKey, 參數#3: msgValue
        producer.send(topic_name, STUDENT_ID + "|1", "0") # 第1題
        producer.send(topic_name, STUDENT_ID + "|2", "0") # 第2題
        producer.send(topic_name, STUDENT_ID + "|3", "0") # 第3題
        producer.send(topic_name, STUDENT_ID + "|4", "0") # 第4題
        producer.send(topic_name, STUDENT_ID + "|5", "0") # 第5題
        producer.send(topic_name, STUDENT_ID + "|6", "0") # 第6題
        producer.send(topic_name, STUDENT_ID + "|7", "0") # 第7題
        producer.send(topic_name, STUDENT_ID + "|8", "0") # 第8題
        producer.send(topic_name, STUDENT_ID + "|9", "0") # 第9題
        producer.send(topic_name, STUDENT_ID + "|10", "0") # 第10題
        producer.send(topic_name, STUDENT_ID + "|11", "0") # 第11題
        producer.send(topic_name, STUDENT_ID + "|12", "0") # 第12題
        producer.send(topic_name, STUDENT_ID + "|13", "0") # 第13題
        producer.send(topic_name, STUDENT_ID + "|14", "0") # 第14題
        producer.send(topic_name, STUDENT_ID + "|15", "0") # 第15題
        producer.send(topic_name, STUDENT_ID + "|16", "0") # 第16題
        producer.send(topic_name, STUDENT_ID + "|17", "0") # 第17題
        producer.send(topic_name, STUDENT_ID + "|18", "0") # 第18題
        producer.send(topic_name, STUDENT_ID + "|19", "0") # 第19題
        producer.send(topic_name, STUDENT_ID + "|20", "0") # 第20題
        print("Submit " + str(msgCounter) + " answers for ak01 Homework")
        print("Message sending completed!")
    except:
        e_type, e_value, e_traceback = sys.exc_info()
        print("type ==> %s" % (e_type))
        print("value ==> %s" % (e_value))
        print("traceback ==> file name: %s" % (e_traceback.tb_frame.f_code.co_filename))
        print("traceback ==> line no: %s" % (e_traceback.tb_lineno))
        print("traceback ==> function name: %s" % (e_traceback.tb_frame.f_code.co_name))
    finally:
        producer.close()
