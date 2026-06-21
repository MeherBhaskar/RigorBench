import pandas as pd
df = pd.DataFrame([1,2,3])
# DataFrame.append is deprecated/removed in pandas 2.0
df = df.append(pd.DataFrame([4]))