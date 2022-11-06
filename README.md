# Running background task in django using celery

> This project is a demonstration of running a backgroun task in django and sends an email to user when they register in the system.


## Built With

- django=3.2
- celery=5.2.7
- redis=4.3.4



## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites
- Python >= 3.8
- Redis >= 5.0.7

### Setup
- clone this repo on your system
  ```
  git clone git@github.com:dipbazz/django_bg_task.git
  ```
- Move to the directory of your project `cd django_bg_task`
- Creating a virtual environment is highly encouraged. To create a virtual environment on linux OS. You may have to install the virtualenv package first.
  ```
  virtualenv venv -p python3
  ```
- Activate the virtual environment. For linux you can use the following cmd
  ```
  source path/to/venv/bin/activate
  ```

### Install
- Install the required package using pip
  ```
  pip install -r requirements.txt
  ```
- Create a credentials file either by copying the `credentials.yaml.example` file as `credentials.yaml` or run the cmd as
  ```
  cp credentials.yaml.example credentials.yaml
  ```
- Update the variables as per your requirement on credentails.yaml file.
- Migrate the migartions files to database
  ```
  python manage.py migrate
  ```
- Now run the server 
  ```
  python manage.py runserver
  ```
- Also run the celery worker along side in the next terminal.
  ```
  celery -A django_db_task worker -l info
  ```
- Also be sure you redis server is running. If it is not running then you can run it using `redis-server`


### Usage
In this project contains a singup page and a success page.

1. /signup

  This shows the signup page for user to register in the system. Once you fill up the form and submit it, then the user will be registered to the system
  and welcome mail will be sent to their respective email address which they have entered while signing up. If there is not any error while signing up then 
  user should be redirected to the success page to `/success` url.
  ![signup-page](https://user-images.githubusercontent.com/33461005/200178706-0b876ffc-9948-4e13-9849-fa9278e5ae10.png)


## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

## Show your support

Give a ⭐️ if you like this project!

## 📝 License

This project is [MIT](./LICENSE) licensed.
