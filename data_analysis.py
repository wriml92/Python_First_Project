import pandas as pd

# 엑셀 파일 불러오기
df = pd.read_excel('data/관서별 5대범죄 발생 및 검거.xlsx')

# DataFrame 출력
print("\n=== 데이터 미리보기 ===")
print(df)

# 데이터 기본 정보 출력
print("\n=== 데이터 기본 정보 ===")
print(df.info()) 