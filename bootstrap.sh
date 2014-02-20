apt-get update
apt-get install -y apache2
apt-get install -y postgresql postgresql-contrib
apt-get install -y python-dev python-pip
pip install -r /vagrant/requirements.txt