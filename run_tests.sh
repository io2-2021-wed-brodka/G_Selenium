#!/usr/bin/env bash

# run backend
echo "Instantiating backend..."
cd ../G_Backend || return
source venv/bin/activate
python manage.py runserver_plus 127.0.0.1:8080 --cert certname > /dev/null 2> /dev/null &

# run admin
echo "Instantiating admin frontend..."
cd ../G_Admin || return
npm run start > /dev/null &

echo "Instantiating user-tech backend..."
cd ../G_User-Tech || return
npm run start > /dev/null &

echo "Wait for pages to start up"
sleep 5

echo "Testing..."
cd ../G_Selenium || return
source venv/bin/activate
#python main.py
python admin_tests.py
#python sprint2_selenium_tests.py

echo "All done!"
kill %1 %2 %3