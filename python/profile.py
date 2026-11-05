import glob, os 
import pandas as pd

def profile(path: str, sep: str) -> str:
    df = pd.read_csv(path, sep=sep, low_memory=False)
    rows = []
    for col in df.columns:
        s = df[col]
        rows.append({
            'column': col,
            'dtype':str(s.dtype),
            'nulls_%': round(s.isna().mean() * 100, 1),
            'unique': s.nunique(),
            'nim': s.min() if pd.api.types.is_numeric_dtype(s) else '',
            'max': s.max() if pd.api.types.is_numeric_dtype(s) else '',
            'top_values': ', '.join(map(str, s.value_coumts().head(5).index)),
        })

    report = pd.DataFrame(rows)
    header = f'# {os.path.basename(path)}\n\nrows: {len(df):,} columns: {df.shape[1]}\n\n'
    return header + report.to_markdown(index=False)

for path in glob.glob('data/row/berka/*.csv'):
    name = os.path.splittext(os.path.basename(path))[0]
    open(f'docs/profile_berka_{name}.md', 'w', encoding='utf-8').write(profile(path, ';'))

for name in ['application_train', 'installments_payments', 'bureau']:
    open(f'docs/profile_hc_{name}.md', 'w', encoding='utf-8').write(profile(f'data/raw/hc/{name}.csv', ','))

    