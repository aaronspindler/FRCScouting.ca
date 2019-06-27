source FRCScouting_Project/FRCScoutingenv/bin/activate
rm -r FRCScouting_Project/FRCScouting.ca/FRCScouting/static

cd FRCScouting_Project/FRCScouting.ca
git pull

pip install -r requirements.txt

cd FRCScouting

python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate

cd ..

sudo systemctl restart gunicorn
