cd /home
git pull
find /home -not -path "*/.*/*" -not -name ".*" | while read filename
do
	owner=$(echo ${filename#/home/} | cut -f1 -d"/")
	echo $owner
	echo $filename
	chown $owner "$filename"
done
git stage -A
git commit -m "automated backup"
git push
