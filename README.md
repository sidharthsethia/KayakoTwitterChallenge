# Kayako Twitter Challenge

A simple python Twitter client that fetches tweets that have been retweeted and contain the hashtag: #custserv

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.6.1
TwitterSearch
flask
gunicorn
```

### Installing

- Extract the downloaded file
- Move it to your document root
- Add your twitter API secrets in `app/config/config.ini`
- Run app/run.py
- Open browser and navigate to localhost
- The tweets will be fetched and displayed

## Deployment

- Download the Heroku CLI
- Enter `heroku login` in terminal and provide your Heroku credentials
- Set up the app on github
- Make sure you have requirements.txt, runtime.txt and Procfile
- Create a heroku instance in terminal using `heroku create`
- Push the changes to heroku using the command `git push heroku master` to deploy the application
- Ensure that at least one instance of the app is running: `heroku ps:scale web=1`

This app is deployed currently as https://nameless-coast-82870.herokuapp.com

## Built With

* [flask](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Heroku](https://maven.apache.org/) - Web hosting

## Authors

* **Sidharth Sethia** - sethiasidharth@gmail.com

## Acknowledgments

* Thank you Kayako for inspiring to build my first web application or my first web product
