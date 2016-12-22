Run whatsnext.py to get a list of upcoming artists in A2 and Cosmonavt
(with dates and first price found, if any)

```
virtualenv --python=python3 --no-site-packages venv
source venv/bin/activate
pip install -r pip-requirements.txt
python whatsnext.py
```

Example output (22 Dec 2016):
```
A2	28 Dec	Балет «Щелкунчик»	500р
A2	03 Jan	Frost Fest-2017	1400р
A2	04 Jan	Ногу Свело!	500р
A2	05 Jan	RETROMEGADANCE.RU	500р
A2	07 Jan	Christmas Record club	билеты пока не поступили в продажу.
A2	27 Jan	Jay-Jay Johanson	500р
A2	28 Jan	MONOMARK NIGHT 2017	800р
A2	04 Feb	Architects	1500р
...
```
