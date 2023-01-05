@echo off

color 02

echo Prepping raw data...

timeout 5

ren *.csv Work_Emails_Raw.csv

echo Raw Data prepped for refinement

echo Beginning data manipulation

echo excuting Python Script

python main.py

echo Finishing...

echo File output to location: %cd%

pause
