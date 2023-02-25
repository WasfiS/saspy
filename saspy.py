import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from sas7bdat import SAS7BDAT

# import platform
# print('Python: ', platform.python_version())
# print('pandas: ', pd.__version__)
# print('pyarrow: ', pa.__version__)

with SAS7BDAT('/Users/wasfisamodien/Downloads/pss1718_pu_sas7bdat/pss1718_pu.sas7bdat', skip_header=False) as reader:
    df = reader.to_data_frame()

df = df.rename(columns={'PFNLWT': 'column1'})
df = df.loc[:,['column1', 'REPW1']]

df.info(verbose=True)
print(df.head())

with SAS7BDAT('/Users/wasfisamodien/Downloads/pss1718_pu_sas7bdat/pss1718_pu.sas7bdat', skip_header=False) as reader:
    reader.convert_file('/Users/wasfisamodien/Downloads/pss1718_pu_sas7bdat/pss1718_pu2.csv', delimiter=',')

