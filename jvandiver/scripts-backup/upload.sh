#!/bin/bash

aws s3 ls
aws s3 rm s3://gwc-ng-2018-2019/$(whoami) --recursive

find ~ -type f -not -path "*/.*/*" -not -name ".*" | while read filename
do
    editedName=$(echo $filename | sed 's:^/home/::')
    echo $filename
    echo ${editedName}
    aws s3 cp "$filename" "s3://gwc-ng-2018-2019/$editedName" --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers
done
