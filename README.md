# Project 6: Brevet time calculator service

Simple listing service from project 5 stored in MongoDB database.

## ACP controle times

Controls are points where a rider must obtain proof of passage, and control times are the minimum and maximum times by which the rider must arrive at the location.

The algorithm for calculating controle times is described here (https://rusa.org/pages/acp-brevet-control-times-calculator).

Additional background information is given here (https://rusa.org/pages/rulesForRiders).  

This is a replacement of the calculator here (https://rusa.org/octime_acp.html).

## AJAX Flask and Mongo implementation

This code fills in times as the input fields are filled using Ajax and Flask.

Each time a distance is filled in, the corresponding open and close times are filled in with Ajax.

The submit button is then used to store valid control times in a mongodb database, making sure not to add duplicates. This database can be accessed and viewed on a separate page by clicking the display button.

## New Functionalities

This project adds the following four parts to project 5:

* RESTful service to expose what is stored in MongoDB. Specifically the following three basic APIs:
    * "http://<host:port>/listAll" should return all open and close times in the database
    * "http://<host:port>/listOpenOnly" should return open times only
    * "http://<host:port>/listCloseOnly" should return close times only

* Two different representations: one in csv and one in json. JSON is the default representation for the above three basic APIs.
    * "http://<host:port>/listAll/csv" should return all open and close times in CSV format
    * "http://<host:port>/listOpenOnly/csv" should return open times only in CSV format
    * "http://<host:port>/listCloseOnly/csv" should return close times only in CSV format
    * "http://<host:port>/listAll/json" should return all open and close times in JSON format
    * "http://<host:port>/listOpenOnly/json" should return open times only in JSON format
    * "http://<host:port>/listCloseOnly/json" should return close times only in JSON format

* A query parameter to get top "k" open and close times.

    * "http://<host:port>/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format
    * "http://<host:port>/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format
    * "http://<host:port>/listCloseOnly/csv?top=6" should return top 5 close times only (in ascending order) in CSV format
    * "http://<host:port>/listCloseOnly/json?top=4" should return top 4 close times only (in ascending order) in JSON format

* A consumer program to use the services above using PHP. The program is in the "website" container.

## Testing

To run the server, change to the DockerRestAPI directory and type:

- $ sudo make

To exit the server hit:

- ctrl c

After closing the server, remove everything made by up:

- $ sudo make down

To remove docker images and containers:

- $ sudo make prune

### Notes:

Keep in mind that you will need docker and docker-compose installed on your local machine.

If you hit the display button, the values are removed from the db and will not show up on localhost:5000 until submitted again. This was to prevent the database from keeping old values when the user submits new ones, but could be an issue depending on what you expect from the functionality.

The MongoClient settings in flask_brevets.py are hardcoded to a specific IP. I could not get the program to work otherwise. If this does not work on your local machine, I would suggest changing line 20.
From:
client = MongoClient("172.20.0.2", 27017)
To:
client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)

- To access the brevets calculator, go to localhost:5001
- To access the "website" (consumer program) go to localhost:5000

## Authors

####Samuel Lundquist - slundqui@uoregon.edu
