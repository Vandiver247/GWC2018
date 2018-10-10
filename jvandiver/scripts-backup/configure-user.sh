mkdir /home/$1/.ssh
mkdir /home/$1/.aws
chmod 700 /home/$1/.ssh

cp /uploadscripts/.ssh/* /home/$1/.ssh
cp /uploadscripts/.aws/* /home/$1/.aws

chmod 600 /home/$1/.ssh/*

chown $1 /home/$1/.ssh
chown $1 /home/$1/.ssh/*
chown $1 /home/$1/.aws
chown $1 /home/$1/.aws/*
