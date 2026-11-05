# bureau.csv

rows: 1,716,428 columns: 17

| column                 | dtype   |   nulls_% |   unique |              nim |              max | top_values                                                  |
|:-----------------------|:--------|----------:|---------:|-----------------:|-----------------:|:------------------------------------------------------------|
| SK_ID_CURR             | int64   |       0   |   305811 |  100001          | 456255           | 120860, 169704, 318065, 251643, 425396                      |
| SK_ID_BUREAU           | int64   |       0   |  1716428 |       5e+06      |      6.84346e+06 | 5714462, 5714463, 5714464, 5714465, 5714466                 |
| CREDIT_ACTIVE          | str     |       0   |        4 |                  |                  | Closed, Active, Sold, Bad debt                              |
| CREDIT_CURRENCY        | str     |       0   |        4 |                  |                  | currency 1, currency 2, currency 3, currency 4              |
| DAYS_CREDIT            | int64   |       0   |     2923 |   -2922          |      0           | -364, -336, -273, -357, -343                                |
| CREDIT_DAY_OVERDUE     | int64   |       0   |      942 |       0          |   2792           | 0, 30, 60, 8, 13                                            |
| DAYS_CREDIT_ENDDATE    | float64 |       6.1 |    14096 |  -42060          |  31199           | 0.0, 3.0, -7.0, 1.0, -14.0                                  |
| DAYS_ENDDATE_FACT      | float64 |      36.9 |     2917 |  -42023          |      0           | -329.0, -273.0, -301.0, -91.0, -84.0                        |
| AMT_CREDIT_MAX_OVERDUE | float64 |      65.5 |    68251 |       0          |      1.15987e+08 | 0.0, 1440.0, 225.0, 45.0, 4.5                               |
| CNT_CREDIT_PROLONG     | int64   |       0   |       10 |       0          |      9           | 0, 1, 2, 3, 4                                               |
| AMT_CREDIT_SUM         | float64 |       0   |   236708 |       0          |      5.85e+08    | 0.0, 225000.0, 135000.0, 450000.0, 90000.0                  |
| AMT_CREDIT_SUM_DEBT    | float64 |      15   |   226537 |      -4.7056e+06 |      1.701e+08   | 0.0, 4.5, -450.0, 135000.0, 90000.0                         |
| AMT_CREDIT_SUM_LIMIT   | float64 |      34.5 |    51726 | -586406          |      4.7056e+06  | 0.0, 135000.0, 4500.0, 45000.0, 90000.0                     |
| AMT_CREDIT_SUM_OVERDUE | float64 |       0   |     1616 |       0          |      3.75668e+06 | 0.0, 4.5, 9.0, 13.5, 18.0                                   |
| CREDIT_TYPE            | str     |       0   |       15 |                  |                  | Consumer credit, Credit card, Car loan, Mortgage, Microloan |
| DAYS_CREDIT_UPDATE     | int64   |       0   |     2982 |  -41947          |    372           | -7, -8, -11, -15, -12                                       |
| AMT_ANNUITY            | float64 |      71.5 |    40321 |       0          |      1.18453e+08 | 0.0, 4500.0, 13500.0, 22500.0, 9000.0                       |