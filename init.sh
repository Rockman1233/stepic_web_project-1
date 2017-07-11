sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/gunicorndjango.conf /etc/gunicorn.d/testdj
sudo /etc/init.d/gunicorn restart
#sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello:app
#sudo gunicorn -c /home/box/web/etc/gunicorn_django.conf ask.wsgi:application
sudo /etc/init.d/mysql start
