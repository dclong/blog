UUID: 014698ae-5458-4c6f-83b7-0a20b14c6c25
Status: published
Date: 2015-05-17 17:05:55
Author: Ben Chuanlong Du
Slug: generating-yyyymm-formatted-dates-using-python
Title: Generating YYYYMM Formatted Dates Using Python
Category: Computer Science
Tags: programming, Python, credit risk, risk capital, stress testing, YYYYMM, YYYYQQ
Modified: 2015-05-17 17:05:55

```Python

import monthdelta as md
import datetime as dt
import math as math

def quarter(month):
    return int(math.ceil(month/3.0))
#end def

d0 = md.date.today()
dates = [d0 + md.monthdelta(i) for i in range(1, 20)]
yyyymms = [d.year*100 + d.month for d in dates]
yymms = [d.year%100 * 100 + d.month for d in dates]
print(", ".join(map(str, yyyymms)))
print(", ".join(map(str, yymms)))
```

The between ... and clause is also convenient to work with YYYYMM numbers
I saw people use 
```SAS
where m in &months.;
```
to check ..
while a much more convenient way is to use 
```SAS
where m between 200201 and 201212;
```
if you are sure `m` contains only YYYYMM formated numbers.

