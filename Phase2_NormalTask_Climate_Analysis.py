import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

     

daily_data = pd.read_csv("/content/daily_data.csv")
hourly_data = pd.read_csv("/content/hourly_data.csv", low_memory=False)
monthly_data = pd.read_csv("/content/monthly_data.csv")
three_hour_data = pd.read_csv("/content/three_hour_data.csv")

     

for i, data in enumerate([daily_data, hourly_data, monthly_data, three_hour_data]):
    print(f"\nDataset {i+1} Info:")
    print(data.head())
    print(data.info())
    print(data.describe())

     
Dataset 1 Info:
       STATION                DATE REPORT_TYPE  SOURCE BackupElements  \
0  72518014735 2015-01-01 23:59:00       SOD         6         PRECIP   
1  72518014735 2015-01-02 23:59:00       SOD         6         PRECIP   
2  72518014735 2015-01-03 23:59:00       SOD         6         PRECIP   
3  72518014735 2015-01-04 23:59:00       SOD         6         PRECIP   
4  72518014735 2015-01-05 23:59:00       SOD         6         PRECIP   

   BackupElevation BackupEquipment  BackupLatitude  BackupLongitude  \
0              260         PLASTIC         42.6918        -73.83109   
1              260         PLASTIC         42.6918        -73.83109   
2              260         PLASTIC         42.6918        -73.83109   
3              260         PLASTIC         42.6918        -73.83109   
4              260         PLASTIC         42.6918        -73.83109   

       BackupName  ...  DailyPeakWindDirection  DailyPeakWindSpeed  \
0  NWS ALBANY, NY  ...                   190.0                26.0   
1  NWS ALBANY, NY  ...                   250.0                30.0   
2  NWS ALBANY, NY  ...                   170.0                21.0   
3  NWS ALBANY, NY  ...                   290.0                33.0   
4  NWS ALBANY, NY  ...                   280.0                42.0   

   DailyPrecipitation  DailySnowDepth  DailySnowfall  \
0                0.00             0.0            0.0   
1                   T             0.0              T   
2                0.57             0.0            1.6   
3                0.22             1.0            0.0   
4                   T             0.0              T   

   DailySustainedWindDirection  DailySustainedWindSpeed  Sunrise  Sunset  \
0                        190.0                     20.0    726.0  1632.0   
1                        310.0                     23.0    726.0  1633.0   
2                        160.0                     15.0    726.0  1634.0   
3                        290.0                     24.0    726.0  1635.0   
4                        290.0                     32.0    726.0  1636.0   

   WindEquipmentChangeDate  
0               2006-09-08  
1               2006-09-08  
2               2006-09-08  
3               2006-09-08  
4               2006-09-08  

[5 rows x 32 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2668 entries, 0 to 2667
Data columns (total 32 columns):
 #   Column                                      Non-Null Count  Dtype         
---  ------                                      --------------  -----         
 0   STATION                                     2668 non-null   int64         
 1   DATE                                        2668 non-null   datetime64[ns]
 2   REPORT_TYPE                                 2668 non-null   object        
 3   SOURCE                                      2668 non-null   int64         
 4   BackupElements                              2668 non-null   object        
 5   BackupElevation                             2668 non-null   int64         
 6   BackupEquipment                             2668 non-null   object        
 7   BackupLatitude                              2668 non-null   float64       
 8   BackupLongitude                             2668 non-null   float64       
 9   BackupName                                  2668 non-null   object        
 10  DailyAverageDewPointTemperature             2668 non-null   float64       
 11  DailyAverageDryBulbTemperature              2668 non-null   float64       
 12  DailyAverageRelativeHumidity                2668 non-null   float64       
 13  DailyAverageSeaLevelPressure                2668 non-null   float64       
 14  DailyAverageStationPressure                 2668 non-null   float64       
 15  DailyAverageWetBulbTemperature              2668 non-null   float64       
 16  DailyAverageWindSpeed                       2668 non-null   float64       
 17  DailyCoolingDegreeDays                      2668 non-null   float64       
 18  DailyDepartureFromNormalAverageTemperature  2668 non-null   float64       
 19  DailyHeatingDegreeDays                      2668 non-null   float64       
 20  DailyMaximumDryBulbTemperature              2668 non-null   float64       
 21  DailyMinimumDryBulbTemperature              2668 non-null   float64       
 22  DailyPeakWindDirection                      2668 non-null   float64       
 23  DailyPeakWindSpeed                          2668 non-null   float64       
 24  DailyPrecipitation                          2668 non-null   object        
 25  DailySnowDepth                              2668 non-null   object        
 26  DailySnowfall                               2668 non-null   object        
 27  DailySustainedWindDirection                 2668 non-null   float64       
 28  DailySustainedWindSpeed                     2668 non-null   float64       
 29  Sunrise                                     2668 non-null   float64       
 30  Sunset                                      2668 non-null   float64       
 31  WindEquipmentChangeDate                     2668 non-null   object        
dtypes: datetime64[ns](1), float64(20), int64(3), object(8)
memory usage: 667.1+ KB
None
            STATION                           DATE  SOURCE  BackupElevation  \
count  2.668000e+03                           2668  2668.0           2668.0   
mean   7.251801e+10  2018-10-01 14:07:27.346326784     6.0            260.0   
min    7.251801e+10            2015-01-01 23:59:00     6.0            260.0   
25%    7.251801e+10            2016-11-29 17:59:00     6.0            260.0   
50%    7.251801e+10            2018-10-02 11:59:00     6.0            260.0   
75%    7.251801e+10            2020-08-03 05:59:00     6.0            260.0   
max    7.251801e+10            2022-05-31 23:59:00     6.0            260.0   
std    0.000000e+00                            NaN     0.0              0.0   

       BackupLatitude  BackupLongitude  DailyAverageDewPointTemperature  \
count     2668.000000      2668.000000                      2668.000000   
mean        42.689750       -73.828268                        38.217766   
min         42.681200       -73.831090                       -19.000000   
25%         42.691800       -73.831090                        24.000000   
50%         42.691800       -73.831090                        38.000000   
75%         42.691800       -73.831090                        55.000000   
max         42.691800       -73.816500                        73.000000   
std          0.004187         0.005764                        19.116250   

       DailyAverageDryBulbTemperature  DailyAverageRelativeHumidity  \
count                     2668.000000                   2668.000000   
mean                        50.107571                     66.085082   
min                         -3.000000                     24.000000   
25%                         35.000000                     57.000000   
50%                         51.000000                     66.000000   
75%                         67.000000                     76.000000   
max                         87.000000                    100.000000   
std                         18.747310                     13.401359   

       DailyAverageSeaLevelPressure  ...  \
count                   2668.000000  ...   
mean                      30.031945  ...   
min                       29.240000  ...   
25%                       29.880000  ...   
50%                       30.020000  ...   
75%                       30.180000  ...   
max                       30.740000  ...   
std                        0.223771  ...   

       DailyDepartureFromNormalAverageTemperature  DailyHeatingDegreeDays  \
count                                 2668.000000             2668.000000   
mean                                     2.155660               17.040480   
min                                    -28.700000                0.000000   
25%                                     -3.200000                0.000000   
50%                                      1.900000               14.000000   
75%                                      7.200000               30.000000   
max                                     34.700000               68.000000   
std                                      8.202932               16.134205   

       DailyMaximumDryBulbTemperature  DailyMinimumDryBulbTemperature  \
count                     2668.000000                     2668.000000   
mean                        59.418666                       40.299100   
min                          5.000000                      -13.000000   
25%                         42.000000                       27.000000   
50%                         60.000000                       40.000000   
75%                         77.000000                       55.250000   
max                         97.000000                       77.000000   
std                         20.003706                       18.122395   

       DailyPeakWindDirection  DailyPeakWindSpeed  \
count             2668.000000         2668.000000   
mean               222.387556           25.513493   
min                 10.000000            6.000000   
25%                170.000000           19.000000   
50%                260.000000           24.000000   
75%                290.000000           31.000000   
max                360.000000           70.000000   
std                 90.828564            9.436276   

       DailySustainedWindDirection  DailySustainedWindSpeed      Sunrise  \
count                  2668.000000              2668.000000  2668.000000   
mean                    223.924288                19.023238   563.145427   
min                      10.000000                 5.000000   416.000000   
25%                     170.000000                14.000000   447.000000   
50%                     270.000000                18.000000   547.000000   
75%                     290.000000                23.000000   650.000000   
max                     360.000000                67.000000   726.000000   
std                      90.846564                 6.942113   108.536855   

            Sunset  
count  2668.000000  
mean   1783.491004  
min    1621.000000  
25%    1658.000000  
50%    1805.000000  
75%    1905.000000  
max    1938.000000  
std     111.230222  

[8 rows x 24 columns]

Dataset 2 Info:
       STATION                DATE REPORT_TYPE  SOURCE BackupElements  \
0  72518014735 2015-01-01 00:51:00       FM-15       7         PRECIP   
1  72518014735 2015-01-01 01:51:00       FM-15       7         PRECIP   
2  72518014735 2015-01-01 02:51:00       FM-15       7         PRECIP   
3  72518014735 2015-01-01 03:51:00       FM-15       7         PRECIP   
4  72518014735 2015-01-01 04:51:00       FM-15       7         PRECIP   

  BackupElevation BackupEquipment  BackupLatitude  BackupLongitude  \
0             260         PLASTIC         42.6918        -73.83109   
1             260         PLASTIC         42.6918        -73.83109   
2             260         PLASTIC         42.6918        -73.83109   
3             260         PLASTIC         42.6918        -73.83109   
4             260         PLASTIC         42.6918        -73.83109   

       BackupName  ... HourlyDryBulbTemperature HourlyPrecipitation  \
0  NWS ALBANY, NY  ...                       22                   0   
1  NWS ALBANY, NY  ...                       22                   0   
2  NWS ALBANY, NY  ...                       20                   0   
3  NWS ALBANY, NY  ...                       19                   0   
4  NWS ALBANY, NY  ...                       21                   0   

  HourlyRelativeHumidity HourlySeaLevelPressure  HourlyStationPressure  \
0                     46                  30.05                  29.72   
1                     48                  30.04                  29.71   
2                     52                  30.03                   29.7   
3                     57                  30.03                   29.7   
4                     52                  30.04                  29.71   

  HourlyVisibility HourlyWetBulbTemperature  HourlyWindDirection  \
0             10.0                       18                  150   
1             10.0                       18                  170   
2             10.0                       16                  180   
3             10.0                       16                  190   
4             10.0                       17                  170   

   HourlyWindSpeed WindEquipmentChangeDate  
0               10                9/8/2006  
1                8                9/8/2006  
2                6                9/8/2006  
3                7                9/8/2006  
4                8                9/8/2006  

[5 rows x 22 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 64729 entries, 0 to 64728
Data columns (total 22 columns):
 #   Column                     Non-Null Count  Dtype         
---  ------                     --------------  -----         
 0   STATION                    64729 non-null  int64         
 1   DATE                       64729 non-null  datetime64[ns]
 2   REPORT_TYPE                64729 non-null  object        
 3   SOURCE                     64729 non-null  int64         
 4   BackupElements             64729 non-null  object        
 5   BackupElevation            64729 non-null  object        
 6   BackupEquipment            64729 non-null  object        
 7   BackupLatitude             64729 non-null  float64       
 8   BackupLongitude            64729 non-null  float64       
 9   BackupName                 64729 non-null  object        
 10  HourlyAltimeterSetting     64729 non-null  object        
 11  HourlyDewPointTemperature  64729 non-null  object        
 12  HourlyDryBulbTemperature   64729 non-null  object        
 13  HourlyPrecipitation        64729 non-null  object        
 14  HourlyRelativeHumidity     64729 non-null  int64         
 15  HourlySeaLevelPressure     64729 non-null  object        
 16  HourlyStationPressure      64729 non-null  object        
 17  HourlyVisibility           64729 non-null  float64       
 18  HourlyWetBulbTemperature   64729 non-null  int64         
 19  HourlyWindDirection        64729 non-null  object        
 20  HourlyWindSpeed            64729 non-null  int64         
 21  WindEquipmentChangeDate    64729 non-null  object        
dtypes: datetime64[ns](1), float64(3), int64(5), object(13)
memory usage: 10.9+ MB
None
            STATION                           DATE        SOURCE  \
count  6.472900e+04                          64729  64729.000000   
mean   7.251801e+10  2018-09-16 02:04:34.334841856      6.994207   
min    7.251801e+10            2015-01-01 00:51:00      6.000000   
25%    7.251801e+10            2016-11-07 02:51:00      7.000000   
50%    7.251801e+10            2018-09-15 14:51:00      7.000000   
75%    7.251801e+10            2020-07-25 06:51:00      7.000000   
max    7.251801e+10            2022-05-31 23:51:00      7.000000   
std    0.000000e+00                            NaN      0.075894   

       BackupLatitude  BackupLongitude  HourlyRelativeHumidity  \
count    64729.000000     64729.000000            64729.000000   
mean        42.689775       -73.828303               66.361538   
min         42.681200       -73.831090                8.000000   
25%         42.691800       -73.831090               53.000000   
50%         42.691800       -73.831090               67.000000   
75%         42.691800       -73.831090               81.000000   
max         42.691800       -73.816500              100.000000   
std          0.004167         0.005736               18.376979   

       HourlyVisibility  HourlyWetBulbTemperature  HourlyWindSpeed  
count      64729.000000              64729.000000     64729.000000  
mean           9.315017                 44.324878         7.556103  
min            0.000000                -14.000000         0.000000  
25%           10.000000                 31.000000         3.000000  
50%           10.000000                 45.000000         7.000000  
75%           10.000000                 60.000000        11.000000  
max           99.420000                 81.000000        43.000000  
std            2.128327                 17.801866         5.735342  

Dataset 3 Info:
       STATION                DATE REPORT_TYPE  SOURCE  AWND BackupElements  \
0  72518014735 2015-01-31 23:59:00       SOM         6   8.9         PRECIP   
1  72518014735 2015-02-28 23:59:00       SOM         6   8.7         PRECIP   
2  72518014735 2015-03-31 23:59:00       SOM         6   9.4         PRECIP   
3  72518014735 2015-04-30 23:59:00       SOM         6   9.4         PRECIP   
4  72518014735 2015-05-31 23:59:00       SOM         6   8.3         PRECIP   

   BackupElevation BackupEquipment  BackupLatitude  BackupLongitude  ...  \
0              260         PLASTIC         42.6918        -73.83109  ...   
1              260         PLASTIC         42.6918        -73.83109  ...   
2              260         PLASTIC         42.6918        -73.83109  ...   
3              260         PLASTIC         42.6918        -73.83109  ...   
4              260         PLASTIC         42.6918        -73.83109  ...   

  MonthlyMeanTemperature  MonthlyMinSeaLevelPressureValue  \
0                   19.7                            29.32   
1                   12.7                            29.56   
2                   29.8                            29.56   
3                   47.8                            29.54   
4                   65.6                            29.71   

   MonthlyMinSeaLevelPressureValueDate  MonthlyMinSeaLevelPressureValueTime  \
0                                 24.0                               1707.0   
1                                 15.0                                151.0   
2                                 17.0                               1251.0   
3                                 21.0                                451.0   
4                                 12.0                               1251.0   

   MonthlyMinimumTemperature  MonthlySeaLevelPressure  MonthlyStationPressure  \
0                       10.5                    30.11                   29.77   
1                        2.4                    30.09                   29.75   
2                       20.7                    30.10                   29.76   
3                       36.9                    29.98                   29.66   
4                       52.8                    30.09                   29.77   

   MonthlyTotalLiquidPrecipitation  NormalsHeatingDegreeDay  \
0                             2.17                   1316.0   
1                             2.15                   1093.0   
2                             1.25                    929.0   
3                             2.10                    520.0   
4                             1.05                    235.0   

   WindEquipmentChangeDate  
0               2006-09-08  
1               2006-09-08  
2               2006-09-08  
3               2006-09-08  
4               2006-09-08  

[5 rows x 46 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 87 entries, 0 to 86
Data columns (total 46 columns):
 #   Column                                        Non-Null Count  Dtype         
---  ------                                        --------------  -----         
 0   STATION                                       87 non-null     int64         
 1   DATE                                          87 non-null     datetime64[ns]
 2   REPORT_TYPE                                   87 non-null     object        
 3   SOURCE                                        87 non-null     int64         
 4   AWND                                          87 non-null     float64       
 5   BackupElements                                87 non-null     object        
 6   BackupElevation                               87 non-null     int64         
 7   BackupEquipment                               87 non-null     object        
 8   BackupLatitude                                87 non-null     float64       
 9   BackupLongitude                               87 non-null     float64       
 10  BackupName                                    87 non-null     object        
 11  CDSD                                          87 non-null     float64       
 12  CLDD                                          87 non-null     float64       
 13  DSNW                                          87 non-null     float64       
 14  HDSD                                          87 non-null     float64       
 15  HTDD                                          87 non-null     float64       
 16  MonthlyDaysWithGT001Precip                    87 non-null     float64       
 17  MonthlyDaysWithGT010Precip                    87 non-null     float64       
 18  MonthlyDaysWithGT32Temp                       87 non-null     float64       
 19  MonthlyDaysWithGT90Temp                       87 non-null     float64       
 20  MonthlyDaysWithLT0Temp                        87 non-null     float64       
 21  MonthlyDaysWithLT32Temp                       87 non-null     float64       
 22  MonthlyDepartureFromNormalAverageTemperature  87 non-null     float64       
 23  MonthlyDepartureFromNormalCoolingDegreeDays   87 non-null     float64       
 24  MonthlyDepartureFromNormalHeatingDegreeDays   87 non-null     float64       
 25  MonthlyDepartureFromNormalMaximumTemperature  87 non-null     float64       
 26  MonthlyDepartureFromNormalMinimumTemperature  87 non-null     float64       
 27  MonthlyDepartureFromNormalPrecipitation       87 non-null     float64       
 28  MonthlyGreatestPrecip                         87 non-null     float64       
 29  MonthlyGreatestPrecipDate                     87 non-null     object        
 30  MonthlyGreatestSnowDepth                      87 non-null     object        
 31  MonthlyGreatestSnowfall                       87 non-null     object        
 32  MonthlyMaxSeaLevelPressureValue               87 non-null     float64       
 33  MonthlyMaxSeaLevelPressureValueDate           87 non-null     float64       
 34  MonthlyMaxSeaLevelPressureValueTime           87 non-null     float64       
 35  MonthlyMaximumTemperature                     87 non-null     float64       
 36  MonthlyMeanTemperature                        87 non-null     float64       
 37  MonthlyMinSeaLevelPressureValue               87 non-null     float64       
 38  MonthlyMinSeaLevelPressureValueDate           87 non-null     float64       
 39  MonthlyMinSeaLevelPressureValueTime           87 non-null     float64       
 40  MonthlyMinimumTemperature                     87 non-null     float64       
 41  MonthlySeaLevelPressure                       87 non-null     float64       
 42  MonthlyStationPressure                        87 non-null     float64       
 43  MonthlyTotalLiquidPrecipitation               87 non-null     float64       
 44  NormalsHeatingDegreeDay                       87 non-null     float64       
 45  WindEquipmentChangeDate                       87 non-null     object        
dtypes: datetime64[ns](1), float64(34), int64(3), object(8)
memory usage: 31.4+ KB
None
            STATION                           DATE  SOURCE       AWND  \
count  8.700000e+01                             87    87.0  87.000000   
mean   7.251801e+10  2018-09-25 12:40:22.758621184     6.0   7.596552   
min    7.251801e+10            2015-01-31 23:59:00     6.0   4.700000   
25%    7.251801e+10            2016-11-15 23:59:00     6.0   6.500000   
50%    7.251801e+10            2018-08-31 23:59:00     6.0   7.400000   
75%    7.251801e+10            2020-08-16 11:59:00     6.0   8.700000   
max    7.251801e+10            2022-05-31 23:59:00     6.0  10.700000   
std    0.000000e+00                            NaN     0.0   1.458930   

       BackupElevation  BackupLatitude  BackupLongitude         CDSD  \
count             87.0       87.000000        87.000000    87.000000   
mean             260.0       42.689729       -73.828239   362.954023   
min              260.0       42.681200       -73.831090     0.000000   
25%              260.0       42.691800       -73.831090     0.000000   
50%              260.0       42.691800       -73.831090   210.000000   
75%              260.0       42.691800       -73.831090   741.000000   
max              260.0       42.691800       -73.816500  1026.000000   
std                0.0        0.004227         0.005819   367.436180   

             CLDD       DSNW  ...  MonthlyMaximumTemperature  \
count   87.000000  87.000000  ...                  87.000000   
mean    60.252874   1.149425  ...                  58.793103   
min      0.000000   0.000000  ...                  23.000000   
25%      0.000000   0.000000  ...                  41.200000   
50%      0.000000   0.000000  ...                  58.700000   
75%    114.000000   2.000000  ...                  76.550000   
max    357.000000   5.000000  ...                  87.400000   
std     92.905706   1.660266  ...                  18.297673   

       MonthlyMeanTemperature  MonthlyMinSeaLevelPressureValue  \
count               87.000000                        87.000000   
mean                49.234483                        29.437701   
min                 12.700000                        28.820000   
25%                 32.900000                        29.335000   
50%                 48.900000                        29.440000   
75%                 66.450000                        29.585000   
max                 76.500000                        29.750000   
std                 17.363701                         0.202672   

       MonthlyMinSeaLevelPressureValueDate  \
count                            87.000000   
mean                             15.620690   
min                               1.000000   
25%                               7.500000   
50%                              15.000000   
75%                              23.500000   
max                              31.000000   
std                               8.977027   

       MonthlyMinSeaLevelPressureValueTime  MonthlyMinimumTemperature  \
count                            87.000000                  87.000000   
mean                           1242.494253                  39.671264   
min                              51.000000                   2.400000   
25%                             701.000000                  24.350000   
50%                            1414.000000                  39.500000   
75%                            1707.500000                  55.550000   
max                            2351.000000                  66.500000   
std                             618.884722                  16.514024   

       MonthlySeaLevelPressure  MonthlyStationPressure  \
count                87.000000               87.000000   
mean                 30.031149               29.691264   
min                  29.860000               28.860000   
25%                  29.975000               29.655000   
50%                  30.030000               29.700000   
75%                  30.090000               29.770000   
max                  30.210000               29.880000   
std                   0.076088                0.136840   

       MonthlyTotalLiquidPrecipitation  NormalsHeatingDegreeDay  
count                        87.000000                87.000000  
mean                          3.377586               573.781609  
min                           0.900000                 5.000000  
25%                           2.205000               144.000000  
50%                           3.070000               520.000000  
75%                           4.095000              1093.000000  
max                           8.960000              1316.000000  
std                           1.602071               459.629563  

[8 rows x 38 columns]

Dataset 4 Info:
       STATION                DATE REPORT_TYPE  SOURCE BackupElements  \
0  72518014735 2015-01-01 01:00:00       FM-12       4         PRECIP   
1  72518014735 2015-01-01 04:00:00       FM-12       4         PRECIP   
2  72518014735 2015-01-01 07:00:00       FM-12       4         PRECIP   
3  72518014735 2015-01-01 10:00:00       FM-12       4         PRECIP   
4  72518014735 2015-01-01 13:00:00       FM-12       4         PRECIP   

   BackupElevation BackupEquipment  BackupLatitude  BackupLongitude  \
0              260         PLASTIC         42.6918        -73.83109   
1              260         PLASTIC         42.6918        -73.83109   
2              260         PLASTIC         42.6918        -73.83109   
3              260         PLASTIC         42.6918        -73.83109   
4              260         PLASTIC         42.6918        -73.83109   

       BackupName  ... HourlyPressureChange HourlyPressureTendency  \
0  NWS ALBANY, NY  ...                 0.09                      8   
1  NWS ALBANY, NY  ...                 0.02                      6   
2  NWS ALBANY, NY  ...                -0.02                      1   
3  NWS ALBANY, NY  ...                -0.01                      3   
4  NWS ALBANY, NY  ...                 0.11                      8   

   HourlyRelativeHumidity  HourlySeaLevelPressure  HourlyStationPressure  \
0                      46                   30.05                  29.72   
1                      57                   30.03                   29.7   
2                      52                   30.05                  29.72   
3                      44                   30.06                  29.72   
4                      38                   29.95                  29.62   

  HourlyVisibility HourlyWetBulbTemperature  HourlyWindDirection  \
0             9.94                       18                  150   
1             9.94                       16                  190   
2             9.94                       17                  160   
3             9.94                       21                  180   
4             9.94                       23                  170   

   HourlyWindSpeed  WindEquipmentChangeDate  
0               10                 9/8/2006  
1                7                 9/8/2006  
2                9                 9/8/2006  
3               11                 9/8/2006  
4               15                 9/8/2006  

[5 rows x 22 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20843 entries, 0 to 20842
Data columns (total 22 columns):
 #   Column                     Non-Null Count  Dtype         
---  ------                     --------------  -----         
 0   STATION                    20843 non-null  int64         
 1   DATE                       20843 non-null  datetime64[ns]
 2   REPORT_TYPE                20843 non-null  object        
 3   SOURCE                     20843 non-null  int64         
 4   BackupElements             20843 non-null  object        
 5   BackupElevation            20843 non-null  int64         
 6   BackupEquipment            20843 non-null  object        
 7   BackupLatitude             20843 non-null  float64       
 8   BackupLongitude            20843 non-null  float64       
 9   BackupName                 20843 non-null  object        
 10  HourlyDewPointTemperature  20843 non-null  object        
 11  HourlyDryBulbTemperature   20843 non-null  object        
 12  HourlyPressureChange       20843 non-null  float64       
 13  HourlyPressureTendency     20843 non-null  int64         
 14  HourlyRelativeHumidity     20843 non-null  int64         
 15  HourlySeaLevelPressure     20843 non-null  object        
 16  HourlyStationPressure      20843 non-null  object        
 17  HourlyVisibility           20843 non-null  float64       
 18  HourlyWetBulbTemperature   20843 non-null  int64         
 19  HourlyWindDirection        20843 non-null  int64         
 20  HourlyWindSpeed            20843 non-null  int64         
 21  WindEquipmentChangeDate    20843 non-null  object        
dtypes: datetime64[ns](1), float64(4), int64(8), object(9)
memory usage: 3.5+ MB
None
            STATION                           DATE   SOURCE  BackupElevation  \
count  2.084300e+04                          20843  20843.0          20843.0   
mean   7.251801e+10  2018-09-15 11:37:46.084537088      4.0            260.0   
min    7.251801e+10            2015-01-01 01:00:00      4.0            260.0   
25%    7.251801e+10            2016-11-08 14:30:00      4.0            260.0   
50%    7.251801e+10            2018-09-14 07:00:00      4.0            260.0   
75%    7.251801e+10            2020-07-23 11:30:00      4.0            260.0   
max    7.251801e+10            2022-05-31 22:00:00      4.0            260.0   
std    0.000000e+00                            NaN      0.0              0.0   

       BackupLatitude  BackupLongitude  HourlyPressureChange  \
count    20843.000000     20843.000000          20843.000000   
mean        42.689777       -73.828305              0.001490   
min         42.681200       -73.831090             -0.320000   
25%         42.691800       -73.831090             -0.030000   
50%         42.691800       -73.831090              0.000000   
75%         42.691800       -73.831090              0.030000   
max         42.691800       -73.816500              0.310000   
std          0.004166         0.005734              0.049271   

       HourlyPressureTendency  HourlyRelativeHumidity  HourlyVisibility  \
count            20843.000000            20843.000000      20843.000000   
mean                 4.907835               66.611524          9.228507   
min                  1.000000                9.000000          0.060000   
25%                  3.000000               53.000000          9.940000   
50%                  5.000000               67.000000          9.940000   
75%                  8.000000               81.000000          9.940000   
max                  9.000000              100.000000          9.940000   
std                  2.762154               18.291543          2.122013   

       HourlyWetBulbTemperature  HourlyWindDirection  HourlyWindSpeed  
count              20843.000000         20843.000000     20843.000000  
mean                  44.113611           178.702682         7.637864  
min                  -14.000000             0.000000         0.000000  
25%                   31.000000            40.000000         3.000000  
50%                   44.000000           180.000000         7.000000  
75%                   60.000000           290.000000        11.000000  
max                   80.000000           360.000000        38.000000  
std                   17.775246           120.209434         5.768944  

# Preprocess daily data
daily_data['DATE'] = pd.to_datetime(daily_data['DATE'])
daily_data.dropna(inplace=True)
daily_data.set_index('DATE', inplace=True)

# Preprocess hourly data
hourly_data['DATE'] = pd.to_datetime(hourly_data['DATE'])
hourly_data.dropna(inplace=True)
hourly_data.set_index('DATE', inplace=True)

# Preprocess monthly data
monthly_data['DATE'] = pd.to_datetime(monthly_data['DATE'])
monthly_data.dropna(inplace=True)
monthly_data.set_index('DATE', inplace=True)

# Preprocess three hour data
three_hour_data['DATE'] = pd.to_datetime(three_hour_data['DATE'])
three_hour_data.dropna(inplace=True)
three_hour_data.set_index('DATE', inplace=True)

     

plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_data, x=daily_data.index, y='DailyAverageDryBulbTemperature')
plt.title('Average Temperature Over Time (Daily)')
plt.xlabel('Date')
plt.ylabel('Temperature (F)')
plt.show()



     


plt.figure(figsize=(12, 6))
sns.lineplot(data=hourly_data, x=hourly_data.index, y='HourlyDryBulbTemperature')
plt.title('Average Temperature Over Time (Hourly)')
plt.xlabel('Date')
plt.ylabel('Temperature (F)')
plt.show()

     


plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_data, x=monthly_data.index, y='MonthlyMeanTemperature')
plt.title('Average Temperature Over Time (Monthly)')
plt.xlabel('Date')
plt.ylabel('Temperature (F)')
plt.show()

     


plt.figure(figsize=(12, 6))
sns.lineplot(data=three_hour_data, x=three_hour_data.index, y='HourlyDryBulbTemperature')
plt.title('Average Temperature Over Time (Three Hour)')
plt.xlabel('Date')
plt.ylabel('Temperature (F)')
plt.show()

     


plt.figure(figsize=(12, 6))
sns.histplot(daily_data['DailyMaximumDryBulbTemperature'], bins=30, kde=True, color='red', label='Max Temperature')
sns.histplot(daily_data['DailyMinimumDryBulbTemperature'], bins=30, kde=True, color='blue', label='Min Temperature')
plt.title('Distribution of Maximum and Minimum Temperatures (Daily)')
plt.xlabel('Temperature (F)')
plt.ylabel('Frequency')
plt.legend()
plt.show()



     


plt.figure(figsize=(12, 6))
sns.histplot(hourly_data['HourlyDryBulbTemperature'], bins=30, kde=True, color='red', label='Max Temperature')
sns.histplot(hourly_data['HourlyDewPointTemperature'], bins=30, kde=True, color='blue', label='Min Temperature')
plt.title('Distribution of Maximum and Minimum Temperatures (Hourly)')
plt.xlabel('Temperature (F)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

     


plt.figure(figsize=(12, 6))
sns.histplot(monthly_data['MonthlyMaximumTemperature'], bins=30, kde=True, color='red', label='Max Temperature')
sns.histplot(monthly_data['MonthlyMinimumTemperature'], bins=30, kde=True, color='blue', label='Min Temperature')
plt.title('Distribution of Maximum and Minimum Temperatures (Monthly)')
plt.xlabel('Temperature (F)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

     


plt.figure(figsize=(12, 6))
sns.histplot(three_hour_data['HourlyDryBulbTemperature'], bins=30, kde=True, color='red', label='Max Temperature')
sns.histplot(three_hour_data['HourlyDewPointTemperature'], bins=30, kde=True, color='blue', label='Min Temperature')
plt.title('Distribution of Maximum and Minimum Temperatures (Three Hour)')
plt.xlabel('Temperature (F)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

     


import numpy as np

plt.figure(figsize=(10, 6))

# Filter out non-numeric values and convert to float
temp_daily = daily_data['DailyAverageDryBulbTemperature']
temp_hourly = hourly_data['HourlyDryBulbTemperature']
temp_monthly = monthly_data['MonthlyMeanTemperature']
temp_three_hour = three_hour_data['HourlyDryBulbTemperature']

# Function to convert to float or NaN if conversion fails
def convert_to_float(x):
    try:
        return float(x)
    except ValueError:
        return np.nan

temp_daily = temp_daily.apply(convert_to_float)
temp_hourly = temp_hourly.apply(convert_to_float)
temp_monthly = temp_monthly.apply(convert_to_float)
temp_three_hour = temp_three_hour.apply(convert_to_float)

# Plotting the bar plot
plt.bar(['Daily', 'Hourly', 'Monthly', 'Three Hour'], [temp_daily.mean(), temp_hourly.mean(), temp_monthly.mean(), temp_three_hour.mean()], color=['red', 'blue', 'green', 'orange'])
plt.title('Average Temperature Comparison')
plt.xlabel('Dataset')
plt.ylabel('Average Temperature (F)')
plt.show()

     
