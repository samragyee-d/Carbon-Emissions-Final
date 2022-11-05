#Importing pandas
import pandas as pd

#Establishing a file route
df_carbondata = pd.read_csv(r"C:\Users\Hem Dhakal BCCC\Downloads\Countries and Territories (1).csv")

#Establising variable that will store the emissions data for each income level. 
#Inside the df_carbondata.loc call carbon data, and everything in the brackets get the data based on the income level. 
df_LowIncome = df_carbondata.loc[df_carbondata.IncomeLevel=='Low Income', "Carbon"]
df_LowerMiddleIncome = df_carbondata.loc[df_carbondata.IncomeLevel=='Lower Middle Income', "Carbon"]
df_UpperMiddleIncome = df_carbondata.loc[df_carbondata.IncomeLevel=='Upper Middle Income', "Carbon"]
df_HighIncome = df_carbondata.loc[df_carbondata.IncomeLevel=='High Income', "Carbon"]

#Establising global variables
global sumCO
global lenCO
global avgCO
global rounded_avgCO

#Function with the input as a parameter
#if statement says that if the parameter equals a certain income level (str) then 
# the function should equate the input to the variables established above that holds carbon data. 
# That value is passed to the "sumCO" varibale which equates to a pandas function "sum" that holds 
# the variable with the carbon data. It adds up all of the data in the variable
# that data then goes through the "lenCO" variable which equates to a pandas function "len" that also holds carbon data.
# "len" determines the length of the data
# "avgCO" is a variable that equates to the "sumCO" being divided by the "lenCO" which gives us the average. 
# "avgCO" is then taken to another variable called "rounded_avgCO" which equates to the pandas round function that holds 
# "avgCO". 
#The result is printed
def CalcAvg (InputIncome):
    if InputIncome == "Low Income":
        InputIncome = df_LowIncome
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
result = CalcAvg("Low Income") 

