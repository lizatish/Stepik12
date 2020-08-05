sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/hello
sudo /etc/init.d/nginx restart

