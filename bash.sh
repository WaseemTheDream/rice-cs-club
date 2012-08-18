#!/usr/bin/sh
ALL=`find . -type f`
for file in $ALL
do
	echo "Removing assets path from $file"
	sed -i '' 's/\(<.*".*\)\(assets\/\)\(.*".*>\)/\1\3/g' "$file"
done

