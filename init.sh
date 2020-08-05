sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo -s ln -sf /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart

