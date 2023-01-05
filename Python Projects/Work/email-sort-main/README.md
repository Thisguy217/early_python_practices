# email-sort

This is two scripts found inside environment(because I am not very good at batch or bash scripting) that when executed either via terminal or GUI 
will parse through a Google Admin CSV output of all emails in a given company, I am going go back and adjust so it will take parameters for what to 
do for trimming. This right now is only set up to trim suspended users that have not logged in for 60 days. So with a lot of hard coding it needs to
be adjusted for general purposing, but it should work no matter what.

If you run into any issues with execution, the python file will be the problematic space. It will require pandas, datetime, and time modules. I 
installed time module becuase I realized the script was running so fast people would miss the outputs for small files. The whole set up runs in 
just a few seconds (something like 5 seconds). However, I did add them at just a couple spots to slow down the code. No big deal.

Any questions about optimization or suggestions are welcome.
