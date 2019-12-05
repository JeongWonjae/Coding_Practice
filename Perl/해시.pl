$HashArr{"math"}=80;
$HashArr{"eng"}=100;
$HashArr{"science"}=90;

foreach(keys (%HashArr)){
  print "$_ :", $HashArr{"$_"}, "\n";
}

@keys=keys %HashArr; #키 저장
@values=values %HashArr; #값 저장

while($#keys>=0){
  print pop(@keys), " : ", pop(@values), "\n";
}

print "before\n", print "After\n"; #뒤 먼저 실행됨

print (3+3)*3, "\n\n"; #왜 16이 나올까 ?
print "\n";

#each 함수
%scores=("eng", 100, "math", 50, "music", 80, "geo", 90);
while(($key, $value)=each %scores){
  print "$key :\t$value\n";
}

@tmpArr=%scores;
print "-----------------\n";
print "\@arr : @tmpArr\n";
$count=($#tmpArr+1)/2;
print "$#tmpArr : Number of data in %scores : $count \n";
