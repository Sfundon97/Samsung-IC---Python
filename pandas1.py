#Pandas
import pandas as pd
import chart as ct
def main():
    x = [1, 6, 3, 4, 5, 2]
    y = [1, 2, 3, 4, 5, 6]
    data = {'Student Numbers': [22001, 22002, 22003, 22004],'Student Names': ['John', 'Palesa', 'Tau', 'Inno']}
    y = [str(value) for value in y]
    df = pd.DataFrame(data)
    chat = ct.bar(x, y)
    print(df)
    print(chat)

main()