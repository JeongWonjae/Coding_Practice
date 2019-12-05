
#받은 명령어 개수 컨트롤
if($#ARGV<0){
  die "None parameter.\n";
}
if($#ARGV>5){
  die "Too many parameter.\n";
}

#ARGV 배열에 받은 파라미터 값들을 저장
$i=1;
while($#ARGV>-1){
  $commandWord=shift(@ARGV);
  print "sequence : $i : ", $commandWord, "\n";
  $i=$i+1;
}
