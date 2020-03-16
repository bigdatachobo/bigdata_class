# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:32:11 2019

@author: sundooedu
"""

import numpy as np
import pandas as pd
import matplolib.pyplot as plt
from scipy import stats, polyval # 과학적인 계산 분석 라이브러리



df = pd.DataFrame(np.random.randn(6,4),
                  columns=['A','B','C','D'],
                  index=pd.date_range('20191001',periods=6,freq='D'))

df['A'].cov(df['B'])

# 선형적인 상관성
# corr 절대값이 0.4 이하시 >>> 상관성 낮다.
# corr 절대값이 0.4 ~ 0.6 >>> 보통관계
# corr 절대값이 0.6 이상시 >>> 상관성이 높다.
#  -1 <= 상관계수(r) <= +1 사이의 범위값을 가지고 있다.
df['A'].corr(df['B'])

# 정체 요소 간의 상관성 리턴.
df.corr()
# =============================================================================
#           A         B         C         D
# A  1.000000  0.096498  0.472872 -0.521234
# B  0.096498  1.000000  0.756751  0.092574
# C  0.472872  0.756751  1.000000  0.018253
# D -0.521234  0.092574  0.018253  1.000000
# =============================================================================

df = pd.read_csv("loan.csv", sep=",")

# 필요한 열 발췌 및 결측값 제거하기
df2 = df[["loan_amnt", "loan_status","grade", "int_rate", "term"]]

df2 = df2.dropna(how="any")

# '36개월 대출'과 '60개월 대출'의 대출 총액 파악
term_to_loan_amnt_dict = {}
uniq_terms = df2["term"].unique()

for term in uniq_terms:
    loan_amnt_sum = df2.loc[df2["term"] == term, "loan_amnt"].sum()
    term_to_loan_amnt_dict[term] = loan_amnt_sum
term_to_loan_amnt = pd.Series(term_to_loan_amnt_dict)

# 각 대출 상태(불량/우량)에 따른 대출 등급 분포 파악
total_status_category = df2["loan_status"].unique()
bad_status_category = total_status_category[[1, 3, 4, 5, 6, 8]]
df2["bad_loan_status"] = df2["loan_status"].isin(bad_status_category)
bad_loan_status_to_grades = \
df2.loc[df2["bad_loan_status"] == True, "grade"].value_counts()
bad_loan_status_to_grades.sort_index()

# 대출 총액과 대출 이자율 간의 상관관계 파악
df2["loan_amnt"].corr(df2["int_rate"])
# 0.14502309929883955 (상관성이 낮다.)
45100*3*(1-0.45)
# 선형적인 상관성
# corr 절대값이 0.4 이하시 >>> 상관성 낮다.
# corr 절대값이 0.4 ~ 0.6 >>> 보통관계
# corr 절대값이 0.6 이상시 >>> 상관성이 높다.
#  -1 <= 상관계수(r) <= +1 사이의 범위값을 가지고 있다.

# 파일쓰기
bad_loan_status_to_grades.to_csv("bad_loan_status.csv", sep=",")
