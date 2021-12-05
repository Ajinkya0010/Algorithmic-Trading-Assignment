#Project Info
- Full fledged web app (django)
- Can support User profile creation

#Features
- Asks the user to login or register if not already registered (currently not implemented for assignment)
- For new users
    - After successful login, presents a one time form to the user to enter their Kites api key and Kites Secret key
- For existing users
    - After successful login, presents a form with fields Instrument,Premium,Distance,Buy and Sell quantity
- Places the order through Kites Api and redirects the user to a page which shows all their past orders

#How to Use the App
- Clone the repo
- cd to the folder on command prompt
- run `pip install -r requiremnets.txt`
- run `python manage.py migrate`
- run `python manage.py createsuperuser` and give some username ,email and password. `eg. username- dummy, email- dummy@gmail.com, password- 1234`
- run `python manage.py runserver`
- Visit `127.0.0.1:8000/admin` and login with your above created credentials `eg. username-dummy, password - 1234`
- In new tab, open `127.0.0.1:8000`

#App endpoints
- `127.0.0.1:8000` - To ask permission from the user to authorise this app to use their Kites Api
- `127.0.0.1:8000\register` - To ask for new user's Kites Api Key and Kites Api Secret Key
- `127.0.0.1:8000\placeorder` - To ask for users order (i.e.  Instrument,Premium,Distance...)
- `127.0.0.1:8000\login` - To obtain access token from kites and to place the order
- `127.0.0.1:8000\holdings` - To present to the user his/her current holdings
- `127.0.0.1:8000\orders` - To present to the user his/her pending/queued orders