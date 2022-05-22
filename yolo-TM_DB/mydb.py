import pymysql

'''
#RDS info
# host = #rds endpoint
# port = 3306, 포트 설정 안 바꿨면 3306 고정
# username = rds만들 때 입력한 이름
# database = rds DB 내에서 연결하고 싶은 DB 이름
# password = mysql pwd

# MySQL에 비디오를 저장하기 위해서는
# LONGBLOB형으로 테이블을 만들어주고
# LOAD_FILE( ) 함수를 통해서 저장이 가능합니다.
# 비디오 전체 경로를 적어주면 됩니다.
# 비디오를 서버에 저장 후, 서버의 주소를 넘겨주는 것이 일반적

#conn = pymysql.connect(host='localhost', user='root', password='pwdforsql19', charset='utf8') 
#cursor = conn.cursor()

#DB 생성
#sql = "CREATE DATABASE action" 
#cursor.execute(sql) 
#conn.commit() 

#table 생성
# sql = '*3 CREATE TABLE user (
#    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
#    email varchar(255),
#    department varchar(255)
#    ) 
#
'*3 직접 쓰면 자꾸... 주석 블럭이 사라져서
#cursor.execute(sql) 
#conn.commit()

#table 내 데이터 검색
#sql = "SELECT * FROM user where department = %s" 

#cursor.execute(sql, ("AI")) 
#res = cursor.fetchall() 
#fetchone > 하나의 데이터만 가져옴

#for data in res: 
#        print(data) 

#conn.commit() 

#table 내 데이터 수정

# 특정 변수 안에 sql문을 넣고 execute를 통해 실행하면 되는 듯.
# 쿼리를 잘 사용해야겠다...

# 데이터 삭제
# sql = "DELETE FROM user WHERE email = %s" 
# cursor.execute(sql, ("developer_song@limsee.com")) 
# conn.commit() 
# conn.close()
'''

#database name : action
#table name : report

def insertRecord(dog, startTime, action, duration):
        conn = pymysql.connect(host='localhost', user='root', password='pwdforsql19', db='action', charset='utf8') 
        cursor = conn.cursor()
        sql = "INSERT INTO report (dog_name, date, time, type, duration) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql,(dog, startTime.strftime('%Y-%m-%d'), startTime.strftime('%H:%M:%S'), action, duration)) 
        conn.commit()
        conn.close()

def modifyRecord(startTime, duration):
        #dog_name = dog인 조건 추가해야할지도?
        conn = pymysql.connect(host='localhost', user='root', password='pwdforsql19', db='action', charset='utf8')
        cursor = conn.cursor()
        sql = "UPDATE report SET duration = %s WHERE date = %s and time = %s" 
        cursor.execute(sql, (duration, startTime.strftime('%Y-%m-%d'), startTime.strftime('%H:%M:%S'))) 
        conn.commit()
        conn.close()

def alreadyRecord(startTime):
        conn = pymysql.connect(host='localhost', user='root', password='pwdforsql19', db='action', charset='utf8')
        cursor = conn.cursor()
        sql = "SELECT ifnull(max(duration), 0) duration From report WHERE date = %s and time = %s"
        cursor.execute(sql,(startTime.strftime('%Y-%m-%d'), startTime.strftime('%H:%M:%S')))
        result = cursor.fetchone()
        conn.commit()
        return result[0]



