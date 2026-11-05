# application_train.csv

rows: 307,511 columns: 122

| column                       | dtype   |   nulls_% |   unique |              nim |           max | top_values                                                                                           |
|:-----------------------------|:--------|----------:|---------:|-----------------:|--------------:|:-----------------------------------------------------------------------------------------------------|
| SK_ID_CURR                   | int64   |       0   |   307511 | 100002           | 456255        | 100002, 100003, 100004, 100006, 100007                                                               |
| TARGET                       | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| NAME_CONTRACT_TYPE           | str     |       0   |        2 |                  |               | Cash loans, Revolving loans                                                                          |
| CODE_GENDER                  | str     |       0   |        3 |                  |               | F, M, XNA                                                                                            |
| FLAG_OWN_CAR                 | str     |       0   |        2 |                  |               | N, Y                                                                                                 |
| FLAG_OWN_REALTY              | str     |       0   |        2 |                  |               | Y, N                                                                                                 |
| CNT_CHILDREN                 | int64   |       0   |       15 |      0           |     19        | 0, 1, 2, 3, 4                                                                                        |
| AMT_INCOME_TOTAL             | float64 |       0   |     2548 |  25650           |      1.17e+08 | 135000.0, 112500.0, 157500.0, 180000.0, 90000.0                                                      |
| AMT_CREDIT                   | float64 |       0   |     5603 |  45000           |      4.05e+06 | 450000.0, 675000.0, 225000.0, 180000.0, 270000.0                                                     |
| AMT_ANNUITY                  | float64 |       0   |    13672 |   1615.5         | 258026        | 9000.0, 13500.0, 6750.0, 10125.0, 37800.0                                                            |
| AMT_GOODS_PRICE              | float64 |       0.1 |     1002 |  40500           |      4.05e+06 | 450000.0, 225000.0, 675000.0, 900000.0, 270000.0                                                     |
| NAME_TYPE_SUITE              | str     |       0.4 |        7 |                  |               | Unaccompanied, Family, Spouse, partner, Children, Other_B                                            |
| NAME_INCOME_TYPE             | str     |       0   |        8 |                  |               | Working, Commercial associate, Pensioner, State servant, Unemployed                                  |
| NAME_EDUCATION_TYPE          | str     |       0   |        5 |                  |               | Secondary / secondary special, Higher education, Incomplete higher, Lower secondary, Academic degree |
| NAME_FAMILY_STATUS           | str     |       0   |        6 |                  |               | Married, Single / not married, Civil marriage, Separated, Widow                                      |
| NAME_HOUSING_TYPE            | str     |       0   |        6 |                  |               | House / apartment, With parents, Municipal apartment, Rented apartment, Office apartment             |
| REGION_POPULATION_RELATIVE   | float64 |       0   |       81 |      0.00029     |      0.072508 | 0.035792000000000004, 0.04622, 0.030755, 0.025164, 0.026392000000000002                              |
| DAYS_BIRTH                   | int64   |       0   |    17460 | -25229           |  -7489        | -13749, -13481, -18248, -10020, -10292                                                               |
| DAYS_EMPLOYED                | int64   |       0   |    12574 | -17912           | 365243        | 365243, -200, -224, -199, -230                                                                       |
| DAYS_REGISTRATION            | float64 |       0   |    15688 | -24672           |      0        | -1.0, -7.0, -6.0, -4.0, -2.0                                                                         |
| DAYS_ID_PUBLISH              | int64   |       0   |     6168 |  -7197           |      0        | -4053, -4095, -4046, -4417, -4256                                                                    |
| OWN_CAR_AGE                  | float64 |      66   |       62 |      0           |     91        | 7.0, 6.0, 3.0, 8.0, 2.0                                                                              |
| FLAG_MOBIL                   | int64   |       0   |        2 |      0           |      1        | 1, 0                                                                                                 |
| FLAG_EMP_PHONE               | int64   |       0   |        2 |      0           |      1        | 1, 0                                                                                                 |
| FLAG_WORK_PHONE              | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_CONT_MOBILE             | int64   |       0   |        2 |      0           |      1        | 1, 0                                                                                                 |
| FLAG_PHONE                   | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_EMAIL                   | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| OCCUPATION_TYPE              | str     |      31.3 |       18 |                  |               | Laborers, Sales staff, Core staff, Managers, Drivers                                                 |
| CNT_FAM_MEMBERS              | float64 |       0   |       17 |      1           |     20        | 2.0, 1.0, 3.0, 4.0, 5.0                                                                              |
| REGION_RATING_CLIENT         | int64   |       0   |        3 |      1           |      3        | 2, 3, 1                                                                                              |
| REGION_RATING_CLIENT_W_CITY  | int64   |       0   |        3 |      1           |      3        | 2, 3, 1                                                                                              |
| WEEKDAY_APPR_PROCESS_START   | str     |       0   |        7 |                  |               | TUESDAY, WEDNESDAY, MONDAY, THURSDAY, FRIDAY                                                         |
| HOUR_APPR_PROCESS_START      | int64   |       0   |       24 |      0           |     23        | 10, 11, 12, 13, 14                                                                                   |
| REG_REGION_NOT_LIVE_REGION   | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| REG_REGION_NOT_WORK_REGION   | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| LIVE_REGION_NOT_WORK_REGION  | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| REG_CITY_NOT_LIVE_CITY       | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| REG_CITY_NOT_WORK_CITY       | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| LIVE_CITY_NOT_WORK_CITY      | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| ORGANIZATION_TYPE            | str     |       0   |       58 |                  |               | Business Entity Type 3, XNA, Self-employed, Other, Medicine                                          |
| EXT_SOURCE_1                 | float64 |      56.4 |   114584 |      0.0145681   |      0.962693 | 0.5984686928074158, 0.6677395635616753, 0.7657236984386736, 0.5464264086050881, 0.6227066347478732   |
| EXT_SOURCE_2                 | float64 |       0.2 |   119831 |      8.17362e-08 |      0.855    | 0.2858978721410488, 0.2622583692422573, 0.26525634018619443, 0.15967923350263774, 0.2653117484731741 |
| EXT_SOURCE_3                 | float64 |      19.8 |      814 |      0.000527265 |      0.89601  | 0.746300213050371, 0.7136313997323308, 0.6940926425266661, 0.6706517530862718, 0.6528965519806539    |
| APARTMENTS_AVG               | float64 |      50.7 |     2339 |      0           |      1        | 0.0825, 0.0619, 0.0928, 0.0722, 0.0082                                                               |
| BASEMENTAREA_AVG             | float64 |      58.5 |     3780 |      0           |      1        | 0.0, 0.0818, 0.0545, 0.0727, 0.1091                                                                  |
| YEARS_BEGINEXPLUATATION_AVG  | float64 |      48.8 |      285 |      0           |      1        | 0.9871, 0.9856, 0.9861, 0.9801, 0.9866                                                               |
| YEARS_BUILD_AVG              | float64 |      66.5 |      149 |      0           |      1        | 0.8232, 0.8164, 0.8028, 0.728, 0.7348                                                                |
| COMMONAREA_AVG               | float64 |      69.9 |     3181 |      0           |      1        | 0.0, 0.0079, 0.0078, 0.008, 0.0077                                                                   |
| ELEVATORS_AVG                | float64 |      53.3 |      257 |      0           |      1        | 0.0, 0.08, 0.16, 0.24, 0.12                                                                          |
| ENTRANCES_AVG                | float64 |      50.3 |      285 |      0           |      1        | 0.1379, 0.069, 0.1034, 0.2069, 0.0345                                                                |
| FLOORSMAX_AVG                | float64 |      49.8 |      403 |      0           |      1        | 0.1667, 0.3333, 0.0417, 0.375, 0.125                                                                 |
| FLOORSMIN_AVG                | float64 |      67.8 |      305 |      0           |      1        | 0.2083, 0.375, 0.0417, 0.0833, 0.4167                                                                |
| LANDAREA_AVG                 | float64 |      59.4 |     3527 |      0           |      1        | 0.0, 0.0631, 0.0316, 0.0473, 0.0174                                                                  |
| LIVINGAPARTMENTS_AVG         | float64 |      68.4 |     1868 |      0           |      1        | 0.0504, 0.0672, 0.0756, 0.0588, 0.0841                                                               |
| LIVINGAREA_AVG               | float64 |      50.2 |     5199 |      0           |      1        | 0.0, 0.0512, 0.0702, 0.051, 0.0509                                                                   |
| NONLIVINGAPARTMENTS_AVG      | float64 |      69.4 |      386 |      0           |      1        | 0.0, 0.0039, 0.0077, 0.0116, 0.0154                                                                  |
| NONLIVINGAREA_AVG            | float64 |      55.2 |     3290 |      0           |      1        | 0.0, 0.0012, 0.0044, 0.0022, 0.0031                                                                  |
| APARTMENTS_MODE              | float64 |      50.7 |      760 |      0           |      1        | 0.084, 0.063, 0.0945, 0.0735, 0.0084                                                                 |
| BASEMENTAREA_MODE            | float64 |      58.5 |     3841 |      0           |      1        | 0.0, 0.0566, 0.0849, 0.0642, 0.083                                                                   |
| YEARS_BEGINEXPLUATATION_MODE | float64 |      48.8 |      221 |      0           |      1        | 0.9871, 0.9866, 0.9861, 0.9801, 0.9806                                                               |
| YEARS_BUILD_MODE             | float64 |      66.5 |      154 |      0           |      1        | 0.8301, 0.8236, 0.7387, 0.8171, 0.8105                                                               |
| COMMONAREA_MODE              | float64 |      69.9 |     3128 |      0           |      1        | 0.0, 0.008, 0.0079, 0.0078, 0.0081                                                                   |
| ELEVATORS_MODE               | float64 |      53.3 |       26 |      0           |      1        | 0.0, 0.0806, 0.1611, 0.2417, 0.1208                                                                  |
| ENTRANCES_MODE               | float64 |      50.3 |       30 |      0           |      1        | 0.1379, 0.069, 0.1034, 0.2069, 0.0345                                                                |
| FLOORSMAX_MODE               | float64 |      49.8 |       25 |      0           |      1        | 0.1667, 0.3333, 0.0417, 0.375, 0.125                                                                 |
| FLOORSMIN_MODE               | float64 |      67.8 |       25 |      0           |      1        | 0.2083, 0.375, 0.0417, 0.0833, 0.4167                                                                |
| LANDAREA_MODE                | float64 |      59.4 |     3563 |      0           |      1        | 0.0, 0.0194, 0.0645, 0.0484, 0.0323                                                                  |
| LIVINGAPARTMENTS_MODE        | float64 |      68.4 |      736 |      0           |      1        | 0.0551, 0.0735, 0.0826, 0.0643, 0.0918                                                               |
| LIVINGAREA_MODE              | float64 |      50.2 |     5301 |      0           |      1        | 0.0, 0.053, 0.0532, 0.0529, 0.0533                                                                   |
| NONLIVINGAPARTMENTS_MODE     | float64 |      69.4 |      167 |      0           |      1        | 0.0, 0.0039, 0.0078, 0.0117, 0.0156                                                                  |
| NONLIVINGAREA_MODE           | float64 |      55.2 |     3327 |      0           |      1        | 0.0, 0.0011, 0.0046, 0.0033, 0.0012                                                                  |
| APARTMENTS_MEDI              | float64 |      50.7 |     1148 |      0           |      1        | 0.0833, 0.0625, 0.0937, 0.0729, 0.0083                                                               |
| BASEMENTAREA_MEDI            | float64 |      58.5 |     3772 |      0           |      1        | 0.0, 0.0818, 0.1091, 0.0545, 0.0727                                                                  |
| YEARS_BEGINEXPLUATATION_MEDI | float64 |      48.8 |      245 |      0           |      1        | 0.9871, 0.9861, 0.9856, 0.9866, 0.9801                                                               |
| YEARS_BUILD_MEDI             | float64 |      66.5 |      151 |      0           |      1        | 0.8256, 0.8189, 0.8054, 0.7316, 0.8121                                                               |
| COMMONAREA_MEDI              | float64 |      69.9 |     3202 |      0           |      1        | 0.0, 0.0079, 0.008, 0.0078, 0.0014                                                                   |
| ELEVATORS_MEDI               | float64 |      53.3 |       46 |      0           |      1        | 0.0, 0.08, 0.16, 0.24, 0.12                                                                          |
| ENTRANCES_MEDI               | float64 |      50.3 |       46 |      0           |      1        | 0.1379, 0.069, 0.1034, 0.2069, 0.0345                                                                |
| FLOORSMAX_MEDI               | float64 |      49.8 |       49 |      0           |      1        | 0.1667, 0.3333, 0.0417, 0.375, 0.125                                                                 |
| FLOORSMIN_MEDI               | float64 |      67.8 |       47 |      0           |      1        | 0.2083, 0.375, 0.0417, 0.0833, 0.4167                                                                |
| LANDAREA_MEDI                | float64 |      59.4 |     3560 |      0           |      1        | 0.0, 0.0193, 0.0642, 0.0482, 0.0143                                                                  |
| LIVINGAPARTMENTS_MEDI        | float64 |      68.4 |     1097 |      0           |      1        | 0.0513, 0.0684, 0.077, 0.0599, 0.0855                                                                |
| LIVINGAREA_MEDI              | float64 |      50.2 |     5281 |      0           |      1        | 0.0, 0.0548, 0.0518, 0.052000000000000005, 0.0521                                                    |
| NONLIVINGAPARTMENTS_MEDI     | float64 |      69.4 |      214 |      0           |      1        | 0.0, 0.0039, 0.0078, 0.0116, 0.0155                                                                  |
| NONLIVINGAREA_MEDI           | float64 |      55.2 |     3323 |      0           |      1        | 0.0, 0.0012, 0.0022, 0.0037, 0.0044                                                                  |
| FONDKAPREMONT_MODE           | str     |      68.4 |        4 |                  |               | reg oper account, reg oper spec account, not specified, org spec account                             |
| HOUSETYPE_MODE               | str     |      50.2 |        3 |                  |               | block of flats, specific housing, terraced house                                                     |
| TOTALAREA_MODE               | float64 |      48.3 |     5116 |      0           |      1        | 0.0, 0.057, 0.0547, 0.055, 0.0548                                                                    |
| WALLSMATERIAL_MODE           | str     |      50.8 |        7 |                  |               | Panel, Stone, brick, Block, Wooden, Mixed                                                            |
| EMERGENCYSTATE_MODE          | str     |      47.4 |        2 |                  |               | No, Yes                                                                                              |
| OBS_30_CNT_SOCIAL_CIRCLE     | float64 |       0.3 |       33 |      0           |    348        | 0.0, 1.0, 2.0, 3.0, 4.0                                                                              |
| DEF_30_CNT_SOCIAL_CIRCLE     | float64 |       0.3 |       10 |      0           |     34        | 0.0, 1.0, 2.0, 3.0, 4.0                                                                              |
| OBS_60_CNT_SOCIAL_CIRCLE     | float64 |       0.3 |       33 |      0           |    344        | 0.0, 1.0, 2.0, 3.0, 4.0                                                                              |
| DEF_60_CNT_SOCIAL_CIRCLE     | float64 |       0.3 |        9 |      0           |     24        | 0.0, 1.0, 2.0, 3.0, 4.0                                                                              |
| DAYS_LAST_PHONE_CHANGE       | float64 |       0   |     3773 |  -4292           |      0        | 0.0, -1.0, -2.0, -3.0, -4.0                                                                          |
| FLAG_DOCUMENT_2              | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_3              | int64   |       0   |        2 |      0           |      1        | 1, 0                                                                                                 |
| FLAG_DOCUMENT_4              | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_5              | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_6              | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_7              | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_8              | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_9              | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_10             | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_11             | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_12             | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_13             | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_14             | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_15             | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_16             | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_17             | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_18             | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_19             | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_20             | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| FLAG_DOCUMENT_21             | int64   |       0   |        2 |      0           |      1        | 0, 1                                                                                                 |
| AMT_REQ_CREDIT_BUREAU_HOUR   | float64 |      13.5 |        5 |      0           |      4        | 0.0, 1.0, 2.0, 3.0, 4.0                                                                              |
| AMT_REQ_CREDIT_BUREAU_DAY    | float64 |      13.5 |        9 |      0           |      9        | 0.0, 1.0, 2.0, 3.0, 4.0                                                                              |
| AMT_REQ_CREDIT_BUREAU_WEEK   | float64 |      13.5 |        9 |      0           |      8        | 0.0, 1.0, 2.0, 3.0, 4.0                                                                              |
| AMT_REQ_CREDIT_BUREAU_MON    | float64 |      13.5 |       24 |      0           |     27        | 0.0, 1.0, 2.0, 3.0, 4.0                                                                              |
| AMT_REQ_CREDIT_BUREAU_QRT    | float64 |      13.5 |       11 |      0           |    261        | 0.0, 1.0, 2.0, 3.0, 4.0                                                                              |
| AMT_REQ_CREDIT_BUREAU_YEAR   | float64 |      13.5 |       25 |      0           |     25        | 0.0, 1.0, 2.0, 3.0, 4.0                                                                              |