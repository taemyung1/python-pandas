import csv
import numpy as np


# 파일 입력 
f =open('data1.csv','r')
rdr = csv.reader(f)
rdr_line = []
rdr2_line = []

for line in rdr:
    # 라인 수정할 라인 추출
    rdr_line.append(line[5])
    #print(rdr_line)

# 로직
for line2 in rdr_line:
    # 분리할부분 나누기
    rdr2_line.append(line2.strip().split("("))

result = np.array(rdr2_line)
result = result.reshape(-1)


for line3 in range(387): 
    print(result[line3].pop(0))
    
f.close
