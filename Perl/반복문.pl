%tmpHash=("one", 1, "two", 2, "three", 3);

$total=0;

foreach $i(keys %tmpHash){ #key 함수는 해쉬들의 키값들을 배열로 저장, i값에 저장
  print "$i : ", $tmpHash{$i}, "\n";
  $total += $tmpHash{$i}; #i가 키, $tmpHash{$i}가 값
}
print "Total value is $total";

$i=0;
while ($i<5){
  print "\na";
  $i++;
}

#until은 while의 반대개념으로 조건이 거짓일 동안만 실행
$i=0;
until($i>5){
  print "\nb";
  $i++;
}

do{
  print "\nEnter your password :";
  $password=<STDIN>;
  chop($password); #STDIN으로 입력값을 받으면 리턴문자 (\n)과 같이 저장이 되기
  #때문에 chop 함수를 통해 개행문자를 지워주어야 뒤에서 문자 비교가 가능
} while ($password ne "root"); # ne=not equel; $password인자가 "root"와 같지
#않다면 반복

#do{
#  print "\nEnter your password :";
#  $password=<STDIN>;
#  chop($password);
#} until ($password eq "root");

#redo는 블록의 재실행할때 인수를 증가시키지 않음 for($i=0;~~;i++)에서 i++을 하지
#않는다는 소리

$count=0;
for(1..10){
  print "[$_]Enter your password : ";
  chop($password=<STDIN>);
  if($password eq "root"){
    print "password correted.\n";
    last; #C언어에서 break의 역할
  }
  #chop($password);
  if($password eq "roo"){
    last if($count++>=3);
    print "Almost correted. try again\n";
    redo;
  }
}
