import pandas as pd
import time
from datetime import datetime, date

rawEmails = pd.read_csv("Work_Emails_Raw.csv")

print("Python Execution")
print("Original Data Size: ", rawEmails.size)
print("Data trimming...")

time.sleep(5)
suspendedEmails = rawEmails.drop(rawEmails.index[rawEmails['Status [READ ONLY]'] == 'Active'])

print("First Pass Data Size: ", suspendedEmails.size)
print("Data trimming...")

for i in range(len(suspendedEmails.index)):
    if (date(int(suspendedEmails['Last Sign In [READ ONLY]'].iloc[1][0:4]),int(suspendedEmails['Last Sign In [READ ONLY]'].iloc[1][5:7]),int(suspendedEmails['Last Sign In [READ ONLY]'].iloc[1][8:10]))-date(date.today().year, date.today().month, date.today().day)).days >= 60:
        suspendedEmails.drop(i)

print("Preparing data output...")

timeEmails = suspendedEmails.drop(columns=['Password [Required]',
                                           'Password Hash Function [UPLOAD ONLY]',
                                           'Org Unit Path [Required]',
                                           'New Primary Email [UPLOAD ONLY]',
                                           'Recovery Email',
                                           'Home Secondary Email',
                                           'Work Secondary Email',
                                           'Recovery Phone [MUST BE IN THE E.164 FORMAT]',
                                           'Work Phone',
                                           'Home Phone',
                                           'Mobile Phone',
                                           'Work Address',
                                           'Home Address',
                                           'Employee ID',
                                           'Employee Type',
                                           'Employee Title',
                                           'Manager Email',
                                           'Department',
                                           'Cost Center',
                                           '2sv Enrolled [READ ONLY]',
                                           '2sv Enforced [READ ONLY]',
                                           'Building ID',
                                           'Floor Name',
                                           'Floor Section',
                                           'Change Password at Next Sign-In',
                                           'New Status [UPLOAD ONLY]',
                                           'Status [READ ONLY]',
                                           'Last Sign In [READ ONLY]',
                                           'Email Usage [READ ONLY]',
                                           'Drive Usage [READ ONLY]',
                                           'Total Storage [READ ONLY]'])

print("Final Data Size: ", timeEmails.size)
print("Data compilation...")
time.sleep(10)

timeEmails.to_csv('Mutated_Email.csv')
