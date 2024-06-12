Clone this repo and make the following changes:
......
.github/workflows/actions.yml
this file is a hidden file
uncomment line 6 and 7
you can change the scheduled time by changing cron: "15 14 \* \* \*" for help https://crontab.guru
......
email.py:
change sender and receiver mail add your app password form google https://support.google.com/accounts/answer/185833?hl=en
......
download your portfolio csv file from https://meroshare.cdsc.com.np and save it naming "data.csv" in the same directory , you should replace the already present "data.csv"
......
run final.py
choose l for (Enter what you've got yourself? (y/n))
.......
(not recommended)
you can skip above step if want to enter data manually:
run final.py
choose y for (Enter what you've got yourself? (y/n))
.....
push the changes to github and its automated.
