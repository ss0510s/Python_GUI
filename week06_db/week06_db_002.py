import sqlite3

conn = sqlite3.connect('test.db') # connection 열기
cur = conn.cursor() # cursor 열기
cur.execute("select subject from students where professor = 'kim'") # DML 쿼리 실행

# fetchall() : return이 list
records = cur.fetchall()
print(records)
for record in records:
    print(record[0])

conn.commit() # 트랜잭션 커밋
cur.close() # 커서 닫기
conn.close() # connection 닫기

# DDL
# create table student ( , , ,);

# DML
# select 필드이름, * from 테이블이름;
# select 필드이름, * from 테이블이름 where 조건;

# insert into 테이블 (필드이름) values (값들);

# update 테이블 이름 set 업데이트하려는 코드 where 조건문;

# delete from 테이블 where 조건;