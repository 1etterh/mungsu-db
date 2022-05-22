import pymysql

'''
#RDS info
# host = #rds endpoint
# port = 3306, 포트 설정 안 바꿨면 3306 고정
# username = rds만들 때 입력한 이름
# database = rds DB 내에서 연결하고 싶은 DB 이름
# password = mysql pwd

#database name : action
#table name : report
#It is not final file. It has to change 'conn' with our RDS information

def insertRecord(dog, startTime, action, duration):
        conn = pymysql.connect(host='', user='', password='', db='action', charset='utf8') 
        cursor = conn.cursor()
        sql = "INSERT INTO report (dog_name, date, time, type, duration) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql,(dog, startTime.strftime('%Y-%m-%d'), startTime.strftime('%H:%M:%S'), action, duration)) 
        conn.commit()
        conn.close()

def modifyRecord(startTime, duration):
        #dog_name = dog인 조건 추가해야할지도?
        conn = pymysql.connect(host='', user='', password='', db='action', charset='utf8') 
        cursor = conn.cursor()
        sql = "UPDATE report SET duration = %s WHERE date = %s and time = %s" 
        cursor.execute(sql, (duration, startTime.strftime('%Y-%m-%d'), startTime.strftime('%H:%M:%S'))) 
        conn.commit()
        conn.close()

def alreadyRecord(startTime):
        conn = pymysql.connect(host='', user='', password='', db='action', charset='utf8')
        cursor = conn.cursor()
        sql = "SELECT ifnull(max(duration), 0) duration From report WHERE date = %s and time = %s"
        cursor.execute(sql,(startTime.strftime('%Y-%m-%d'), startTime.strftime('%H:%M:%S')))
        result = cursor.fetchone()
        conn.commit()
        return result[0]



