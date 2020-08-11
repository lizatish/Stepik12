sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart

sudo ln -s /home/box/web/etc/hello_django.py  /etc/gunicorn.d/hello_django.py
sudo gunicorn -c /etc/gunicorn.d/hello_django.py ask.wsgi:application
sudo /etc/init.d/gunicorn restart



