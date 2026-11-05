import glob, os
import pandas as pd

os.makedirs('data/samples/', exist_ok=True)
for path in glob.glob('data/raw/*/*.csv'):
    try:
        df = pd.read_csv(path, nrows=1000, low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(path, nrows=1000, low_memory=False, encoding='cp1252')
    df.to_csv(os.path.join('data/samples/', os.path.basename(path)), index=False)
    print('sample:', os.path.basename(path))