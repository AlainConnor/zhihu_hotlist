python3 ./zhihu_crawler.py

year=`date +%Y `
month=`date +%m `
day=`date +%d `
hour=`date +%H`
now=$year-$month-$day-$hour

git add .
git commit -m "$now"
