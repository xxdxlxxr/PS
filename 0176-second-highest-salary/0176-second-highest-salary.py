import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = sorted(set(employee['salary']))
    
    if len(salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    return pd.DataFrame({'SecondHighestSalary': [salaries[-2]]})