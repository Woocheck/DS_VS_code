import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("PL_GEN_WIATR_20211103_20211202_20211203070532.xlsm",
                   "PL_GEN_WIATR_20211103_20211202_", index_col='Data')

df

plt.figure()

df.plot()
