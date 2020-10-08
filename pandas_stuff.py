import pandas as pd
import seaborn as sns
import numpy as np


planets = sns.load_dataset('planets')
print(planets.describe())

rng = np.random.RandomState(42)
df = pd.DataFrame({'A':rng.rand(5),
                'B':rng.rand(5)})
print(df)
print(df.mean(axis=1))


