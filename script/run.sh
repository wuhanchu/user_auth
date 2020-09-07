if [ ! -d "./log/" ];then
  mkdir ./log
fi

gunicorn -w 8 -b 0.0.0.0:5000 run:appl &
python3 run.py --celery >log/celery_work.log 2>&1  < /dev/null &
python3 run.py --celery --beat >log/celery_beta.log 2>&1  < /dev/null &
