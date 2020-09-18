# Pandas

## Pandas.read_csv() [#](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)

#### arguments
1. `filepath_or_buffer`
	- 스트링의 경우, 절대경로가 필요하다.
	- `url` 가능
	- `pathlib.Path` 객체를 그대로 넘겨줄 수 있다. 이 방법을 사용하면 상대경로를 사용할 수 있다.
	- 파일 스트림 가능
2. `sep=','`
	- 구분자를 선택할 수 있다. 기본값은 `csv`의 `,`이며, `tsv`를 사용할 때는 `\t`를 사용하면 된다. 
3. `parse_dates=False`
	- 다양한 타입을 넣을 수 있다. `datetime` 객체로 변환할 칼럼을 설정한다. 
	- `parse_dates=['date']`: `date` 칼럼을 `datetime` 객체로 가져온다.

#### 예시
```python
import pandas as pd
from pathlib import Path

# working directory 를 기준으로 가져온다. 
PATH_KOREAN_INDEX_TSV = Path('st_data_koreaIndex.tsv')
df = pd.read_csv(PATH_KOREAN_INDEX_TSV, sep='\t', parse_dates=['date'])
``` 	


## Pandas.DataFrame
- `df['column_name]`: 해당 칼럼만 뽑아준다.  
- `df.column_name`: 해당 칼럼만 뽑아준다.  
- `df.reset_index()`: 인덱스 초기화. 특정 칼럼만 뽑아내면 인덱스가 뒤죽박죽이다. 그럴 때 사용한다.   
- `df_kospi = df[df.itemcode == 'KOSPI']`: 특정 행만 뽑아내기  

