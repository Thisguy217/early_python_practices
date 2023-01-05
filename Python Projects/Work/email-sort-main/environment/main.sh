echo "$(tput setaf 2) Prepping raw data..."

timeout 5

ren *.csv Work_Emails_Raw.csv

echo "Raw Data prepped for refinement"

echo "Beginning data manipulation"

echo "Excuting Python Script"

python3 main.py

echo "Finishing..."

set location 

echo "File output to location: $(tput setaf 1) $(pwd) $(tput sgr 0)" 
