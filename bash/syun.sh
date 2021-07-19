proces (){
step=0
while [ True ]
do
    clear

    echo PID" 	"USER"        "VIRT"        "COMAND
    list1=$( ls -t /proc ) 
    arr=($list1)   
    for ((step1=$step;step1<$(($step+10));step1++))
    do
	i=${arr[$step1]} 
	if [[ $i =~ ^[0-9] ]]
	then
	                	if [[ -f "/proc/$i/status" ]] 
				then
				pid=$(grep pid /proc/$i/status | awk '{print$2}')
				virt=$(grep VmSize /proc/$i/status | awk '{print$2}')
				user=$(grep Uid /proc/$i/status | awk '{print$2}')
				comand=$(grep Name /proc/$i/status | awk '{print$2}')
	
				echo $pid"	"$user"        "$virt"        "$comand
				fi
			fi
    done
    read -n 1 -t 4 press
    if [[ $press == q ]]
    then
	    break
    
    elif [[ $press == k ]]
    then
	read -p 'press proc pid ' number
        kill -9 $number

    elif [[ $press == j ]]
    then
	step=$(($step+10))
    
    elif [[ $press == u ]]
    then
	step=$(($step-10))
    fi



    
   
done
}
proces



 






proc (){
step=20
while [ True ] 
do
	list1=$( ls  /proc )
	echo PID"\t"USER"\t"VIRT"\t"COMANDD
	echo bbbbbbbbbbbbbbbbb
	read -n 1 -t 4 press
	echo $press
	echo aaaaaaaaaaaaaaaaaaa
	if [ $press == q ]
	then
		break
	elif [ $press == k ]
	then
		read -p 'press proces pid' number
		echo $number
		kill -9 $number
	elif [ $press == u ]
	then
		echo $press
		step=$(($step+5))
	
	elif [ $press == j ]
	then
		echo $press
		step=$(($step-5))
	fi
	#for i in ${list1[*]}
	echo $step
	for (( step1=$step; step1<$(($step+5)); $step1++ ))
	do
		i=${list1[$step1]}
		echo $i
			if [[ $i =~ ^[0-9] ]]
			then
	                	if [[ -f "/proc/$i/status" ]] 
				then
				pid=$(grep pid /proc/$i/status | awk '{print$2}')
				virt=$(grep VmSize /proc/$i/status | awk '{print$2}')
				user=$(grep Uid /proc/$i/status | awk '{print$2}')
				comand=$(grep Name /proc/$i/status | awk '{print$2}')
	
				echo $pid"\t"$user"\t"$virt"\t"$comand
				fi
			fi
			
	done
	
	clear

done
}

	
