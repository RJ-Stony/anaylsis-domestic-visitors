# 🇰🇷 Domestic Visitors Data Analysis

* 엑셀로 제공되는 국가별 외래객 통계를 자동으로 불러오고,  
* 방문 목적(관광, 상용, 기타)에 따라 데이터를 전처리하는 Python 기반 프로젝트입니다.

---

## 📁 프로젝트 구조

```
anaylsis-domestic-visitors-main/
├── files/
│   ├── 3_1_data_preprocessing_multi_xls.py  # ✅ 방문자 전처리 핵심 스크립트
│   ├── kto_201901.xlsx 등 데이터 파일        # 월별 국가별 방문자 수
│   └── 기타 음악 크롤링/시각화 스크립트     # (본 분석과 직접 무관)
├── .gitignore
└── README.md
```

---

## 🔍 주요 스크립트: `3_1_data_preprocessing_multi_xls.py`

> 📊 2019년 1월의 방한 외래객 데이터를 예시로, 엑셀 파일을 불러와 전처리합니다.

### ✅ 핵심 기능

- `pandas.read_excel()`을 활용해 방문자 통계 불러오기  
- 엑셀 내 불필요한 행/열 제거  
- 관광 / 상용 / 기타 목적별 통계 요약  
- 방문자 수가 0명인 국가 필터링  

### 📌 사용된 엑셀 구조

- 헤더는 2행 (index=1)
- 풋터는 4행 제거
- 사용 컬럼: A ~ G 열

### 💡 코드 예시

```python
import pandas as pd

kto_201901 = pd.read_excel('./data/kto_201901.xlsx',
                           header=1,
                           usecols='A:G',
                           skipfooter=4)

# 기본 통계 출력
print(kto_201901.head())
print(kto_201901.describe())

# 방문자 수가 0명인 국가 필터링
zero_visitor = kto_201901[kto_201901['관광'] == 0]
```

---

## 📦 의의 및 활용 방안

- 다중 엑셀 파일을 정제하고 가공하는 데 기반이 되는 전처리 템플릿
- 관광 정책/마케팅 자료로 활용될 수 있는 국가별 통계 분석 가능
- 향후 월별 데이터를 반복적으로 분석할 수 있도록 확장 가능

---

## ⚙️ 실행 환경

- Python 3.12+
- pandas

---

## 📝 라이선스 및 참고

이 프로젝트는 학습 및 공공 데이터 기반 분석을 목적으로 제작되었습니다.
