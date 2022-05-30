# Description
This is an app where I can display my photos for others to see.A user can click on an image to view the image details. A user can also copy an image link.
# Author
Fridah-kalee
## Setup and installations
* Git clone https://github.com/Fridah-kalee/Photo-Gallery.git to your machine
* Create virtual environment:

    $ python3.9 -m venv virtual
* Activate a virtual environment on terminal:

    $ source virtual/bin/activate
* Install all the requirements found in requirements.txt file.

    $ pip freeze > requirements.txt
* On your terminal run command.

    $ python3.9 manage.py runserver
* Access the live site using the local host provided.

    $ open localhost:8000
* Create database migrations

    $ python3 manage.py makemigrations gallery

    $ python3 manage.py migrate
* Run tests

    $ python3 manage.py test  
## Setting up environment variables
SECRET_KEY= #secret key will be added by default

    DEBUG= #set to false in production

    DB_NAME= #database name

    DB_USER= #database user

    DB_PASSWORD=#database password

    DB_HOST="127.0.0.1"

    MODE= # dev or prod , set to prod during production
    
    ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
## User stories 
As a user i want to be able to:

* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
* Search for different categories of photos. (ie. Adventure, Animals)
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.
## Technology used
* Python version 3.9.5.
* Django
* Bootstrap.
* javascript.
* PSQL database.
* HTML,CSS
## Bugs
There are no know bugs at the moment.
## Contact information

For any further inquiries or contributions or comments, reach me at: Fridah-kalee

## License
MIT License

Copyright (c) 2022 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
