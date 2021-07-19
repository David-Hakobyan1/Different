myfind () {
	finds=$(ls $1)

	for i in ${finds[*]}
	do
		if [ -d "$1/$i" ]
		then
			if [ $i == $2 ]
			then
				echo $1
				fi
				myfind $1/$i $2
		else
		       if [ $i == $2 ]
			then
				echo $1
				break
			fi
		
		fi
	
	done

}
myfind $1 $2

	
