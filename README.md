# todo-rest
TODO Application REST API

## Database

As database PostgreSQL 14 is used.

Here some instruction for Ubuntu, in order to install the last version, and some support library for Python:

```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql postgresql-contrib
sudo apt-get install libpq-dev python3-dev
```

Here the link to the official documentation for more information or other OS:

[PostgreSQL Download](https://www.postgresql.org/download/)