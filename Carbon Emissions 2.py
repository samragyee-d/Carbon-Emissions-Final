from flask import Flask
import pandas as pd


df_carbondata = pd.read_csv(r"C:\Users\Hem Dhakal BCCC\Downloads\Countries and Territories (1).csv")


df_LowIncome = df_carbondata.loc[df_carbondata.IncomeLevel=='Low Income', "Carbon"]
df_LowerMiddleIncome = df_carbondata.loc[df_carbondata.IncomeLevel=='Lower Middle Income', "Carbon"]
df_UpperMiddleIncome = df_carbondata.loc[df_carbondata.IncomeLevel=='Upper Middle Income', "Carbon"]
df_HighIncome = df_carbondata.loc[df_carbondata.IncomeLevel=='High Income', "Carbon"]

global sumCO
global lenCO
global avgCO
global rounded_avgCO

def CalcAvg (InputIncome):
    if InputIncome == "Low Income":
        InputIncome = df_LowIncome.round(1)
        sumCO = sum(df_LowIncome)
        lenCO = len(df_LowIncome)
        avgCO = sumCO/lenCO
        rounded_avgCO = round(avgCO)
        print(rounded_avgCO)
    elif InputIncome == "Lower Middle Income":
        InputIncome = df_LowerMiddleIncome.round(1)
        sumCO = sum(df_LowerMiddleIncome)
        lenCO = len(df_LowerMiddleIncome)
        avgCO = sumCO/lenCO
        rounded_avgCO = round(avgCO)
        print(rounded_avgCO)
    elif InputIncome == "Upper Middle Income":
        InputIncome = df_UpperMiddleIncome
        sumCO = sum(df_UpperMiddleIncome)
        lenCO = len(df_UpperMiddleIncome)
        avgCO = sumCO/lenCO
        rounded_avgCO = round(avgCO)
        print(rounded_avgCO)
    elif InputIncome == "High Income":
        InputIncome = df_HighIncome
        sumCO = sum(df_HighIncome)
        lenCO = len(df_HighIncome)
        avgCO = sumCO/lenCO
        rounded_avgCO = round(avgCO)
        print(rounded_avgCO)
result = CalcAvg("Low Income") 
