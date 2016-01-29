Setting up vagrant and create box with centos name

<<vagrant up centos>>
<<vagrant ssh centos>>

Setting Up Flask
<<yum install epel-release -y>>
<<yum install -y python-pip>>

#INstalling python
<<wget https://www.python.org/ftp/python/3.4.4/Python-3.4.4.tgz>>
<<tar -xvf Python-3.4.4.tgz>>
<<./configure>>
<<make>>
<<make install>>
<<pyhton --version>>
<<vi ~/.bashrc>>
<<export PATH=/usr/local/bin:$PATH>>

#Install setup tool and pip for latest python
<<wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz>>
<<tar -xvf setuptools-1.4.2.tar.gz>>
<<cd setuptools-1.4.2>>
<<python3.4 setup.py install>>
<<curl https://bootstrap.pypa.io/get-pip.py | python3.4 ->>


#Creating User for application with sudo access
<<mkdir /mnt/flaskapp>>
<<cd /mnt/flaskapp>>
#Using Different Pyhton version for project
<<virtualenv -p /usr/local/bin/python3.4 .env>>
<<source .env/bin/activate>>
<<pyhton>> #check pythong version
<<pip install flask>>
<<pip install requests>>


#Creating a sudouser group and 
<<groupadd sudouser>>
<<adduser flaskuser -G sudouser>>
<<visudo>>
#Add sudouser group for sudo permission without password instead of adding individual user
%sudouser       ALL=(ALL)       NOPASSWD: ALL
<<su flaskuser>>
<<cd /mnt/flaskapp>>
#It will give permission access error
<<touch sample>>
#It will allow the operation
<<sudo touch sample>>



Setting on MAc
<<curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python>>
<<sudo easy_install pip>>
<<pip install flask>>