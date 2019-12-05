# "찾을 문자열"=~s/찾을문자열/바꿀문자열/옵션;

$tmp="My name are Wonje Jeong. Wonjae are 25 years old";

#s는 문자열단위로 치환함
if($count=($tmp=~s/are/is/gi)){ #global 옵션, i는 대문자 구별 x
  print "Replaced $count time.\n";
} else {
  print "Failed\n";
}
print "Front : $` Back : $'\n";

#tr은 문자단위로 치환
$tmp="ABCDEFG";
$tmp=~tr/ACD/acd/;
print "$tmp";

# *은 문자로 해석
$tmp="* is not\n";
if($count=($tmp=~tr/*/#/)){
  print "Translated $count char.\n";
} else {
  print "No Translation.\n";
}
print "$tmp";

# -문자는 범위로 인식
$tmp="ABCDEFGHIJKLMNOPQRSVWXYZ";
$tmp=~tr/A-Z/a-z/;
print "$tmp";
