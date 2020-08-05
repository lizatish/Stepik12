sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo -c /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart

