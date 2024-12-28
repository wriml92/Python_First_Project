import pandas as pd

# 범죄 데이터 불러오기
df = pd.read_excel('data/관서별 5대범죄 발생 및 검거.xlsx')

# 경찰서-구 매핑 딕셔너리
police_gu_mapping = {
    '서대문서': '서대문구', '수서서': '강남구', '강서서': '강서구', '서초서': '서초구',
    '서부서': '은평구', '중부서': '중구', '종로서': '종로구', '남대문서': '중구',
    '혜화서': '종로구', '용산서': '용산구', '성북서': '성북구', '동대문서': '동대문구',
    '마포서': '마포구', '영등포서': '영등포구', '성동서': '성동구', '동작서': '동작구',
    '광진서': '광진구', '강북서': '강북구', '금천서': '금천구', '중랑서': '중랑구',
    '강남서': '강남구', '관악서': '관악구', '강동서': '강동구', '종암서': '성북구', 
    '구로서': '구로구', '양천서': '양천구', '송파서': '송파구', '노원서': '노원구', 
    '방배서': '서초구', '은평서': '은평구', '도봉서': '도봉구'
}

# '구별' column 생성
df['구별'] = df['관서명'].map(police_gu_mapping).fillna('구 없음')

# pivot_table을 사용하여 구별 데이터로 변경
df_by_gu = pd.pivot_table(
    df,
    index='구별',
    values=['강간(발생)', '강간(검거)', '강도(발생)', '강도(검거)', 
           '살인(발생)', '살인(검거)', '절도(발생)', '절도(검거)', 
           '폭력(발생)', '폭력(검거)', '소계(발생)', '소계(검거)'],
    aggfunc='sum'
)

# '구 없음' 행 삭제
df_by_gu = df_by_gu.drop('구 없음', axis=0)

# 각 범죄별 검거율 계산
df_by_gu['강간검거율'] = (df_by_gu['강간(검거)'] / df_by_gu['강간(발생)']) * 100
df_by_gu['강도검거율'] = (df_by_gu['강도(검거)'] / df_by_gu['강도(발생)']) * 100
df_by_gu['살인검거율'] = (df_by_gu['살인(검거)'] / df_by_gu['살인(발생)']) * 100
df_by_gu['절도검거율'] = (df_by_gu['절도(검거)'] / df_by_gu['절도(발생)']) * 100
df_by_gu['폭력검거율'] = (df_by_gu['폭력(검거)'] / df_by_gu['폭력(발생)']) * 100
df_by_gu['검거율'] = (df_by_gu['소계(검거)'] / df_by_gu['소계(발생)']) * 100

# 불필요한 컬럼 삭제
del df_by_gu['강간(검거)']
del df_by_gu['강도(검거)']
del df_by_gu['살인(검거)']
del df_by_gu['절도(검거)']
del df_by_gu['폭력(검거)']
del df_by_gu['소계(발생)']
del df_by_gu['소계(검거)']

# 컬럼명 변경
df_by_gu = df_by_gu.rename(columns={
    '강간(발생)': '강간',
    '강도(발생)': '강도',
    '살인(발생)': '살인',
    '절도(발생)': '절도',
    '폭력(발생)': '폭력'
})

# 인구 데이터 불러오기 (index를 구별로 설정)
pop_df = pd.read_csv('data/pop_kor.csv', index_col='구별')

print("\n=== 인구 데이터 미리보기 ===")
print(pop_df)

# DataFrame 병합
df_merged = df_by_gu.join(pop_df)

print("\n=== 병합된 데이터 미리보기 ===")
print(df_merged)

# 검거율 기준 오름차순 정렬
df_sorted = df_merged.sort_values('검거율', ascending=True)

print("\n=== 검거율 기준 오름차순 정렬된 데이터 미리보기 ===")
print(df_sorted)

# 데이터 기본 정보 출력
print("\n=== 최종 데이터 기본 정보 ===")
print(df_sorted.info()) 