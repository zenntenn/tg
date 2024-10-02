rm db.sqlite3
rm accounts/migrations/0*
rm characters/migrations/0*
rm core/migrations/0*
rm game/migrations/0*
rm items/migrations/0*
rm locations/migrations/0*
python manage.py makemigrations
python manage.py migrate
yes yes | python manage.py collectstatic
python manage.py createsuperuser

DIRECTORY="populate_db/"

for FILE in "$DIRECTORY"/*; do
  if [ -f "$FILE" ]; then
  echo "Running $FILE..."
  python manage.py shell < "$FILE"
  fi
done
