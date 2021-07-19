list1=$( cat dav.sh )
step=0
name=""
for i in ${list1[*]}
do
step=$(($step+1))
if [ $step -lt 3 ]
then
name=${name}"_"${i}
fi
if [ $step -eq 3 ]
then
echo $i > ${name}.text 
step=0
name=""
fi
done


