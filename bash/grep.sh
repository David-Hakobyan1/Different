\
list1=$(ls $1)
for i in ${list1[*]}
do
	list2=$(ls $i)
	for j in ${list2[*]}
	do
		echo $j
	done
done	
