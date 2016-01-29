#Flask Application

#Setting up vagrant and create box with centos name
`vagrant up centos`</br>
`vagrant ssh centos`

#Setting Up Flask
`yum install epel-release -y`</br>
`yum install -y python-pip`

#INstalling python
`wget https://www.python.org/ftp/python/3.4.4/Python-3.4.4.tgz`</br>
`tar -xvf Python-3.4.4.tgz`</br>
`./configure`</br>
`make`</br>
`make install`</br>
`pyhton --version`</br>
`vi ~/.bashrc`</br>
`export PATH=/usr/local/bin:$PATH`</br>

#Install setup tool and pip for latest python
`wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz`</br>
`tar -xvf setuptools-1.4.2.tar.gz`</br>
`cd setuptools-1.4.2`</br>
`python3.4 setup.py install`</br>
`curl https://bootstrap.pypa.io/get-pip.py | python3.4 -`</br>

#Creating User for application with sudo access
`mkdir /mnt/flaskapp`</br>
`cd /mnt/flaskapp`</br>

#Using Different Pyhton version for project
`virtualenv -p /usr/local/bin/python3.4 .env`</br>
`source .env/bin/activate`</br>
`pyhton` #check pythong version </br>
`pip install flask` </br>
`pip install requests` </br>

#Creating a sudouser group and 
`groupadd sudouser`</br>
`adduser flaskuser -G sudouser`</br>
`visudo`</br>

#Add sudouser group for sudo permission without password instead of adding individual user
%sudouser       ALL=(ALL)       NOPASSWD: ALL
`su flaskuser`</br>
`cd /mnt/flaskapp`</br>
#It will give permission access error
`touch sample`</br>
#It will allow the operation
`sudo touch sample`</br>

Setting on MAc
`curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python`</br>
`sudo easy_install pip`</br>
`pip install flask`</br>
