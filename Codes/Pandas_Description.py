#  IDS 706 Week 2 assignment - Creating a function to show descriptive statistics for a dataframe
# import pandas as pd
import os


def PandasDesc(df):
    """Code to return a summary of a dataframe and save it to a file"""
    os.remove("./Resources/Summary.md")
    f = open("./Resources/Summary.md", "w", encoding="utf-8")
    f.flush()
    f.write(str(df.describe()))
    f.write("\n")
    f.write(f"""![Graph]({"./Resources/PlotImage.png"})""")
    f.close()
    print("Summary of the dataframe has been saved to Summary.md")
    return df.describe()
