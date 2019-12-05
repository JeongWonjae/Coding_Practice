@tmp=(3, 2, "string", 8);
@tmp2=@tmp[1..3]; #배열에 배열을 복사
$a=123;
#새로운 배열의 크기가 늘어날 경우
@MrgArr=($a, @tmp[2..3], "|", @tmp[0..2]);
print "@MrgArr";

#데이터를 빼서 쓰는 경우
($one, $two, $three, $four)=@MrgArr;
print "\n$one";

#데이터를 할당 후 배열에서 삭제
@tmp=(1, 2, 3, 4);
print "\nBefore ARR > @tmp\n";
$one=shift(@tmp); #맨앞 데이터 할당
$two=pop(@tmp); #맨뒤 데이터 할당
print "After ARR > @tmp\n";
print "one is > $one\ntwo is > $two\n";
push(@tmp, 4);

while($a=pop(@tmp)){
  print "$a\n";
} print "BOMM! @tmp\n";

#원래 배열의 크기가 줄었다가 늘어나는 코드인데 이 버전은 안됨?
@tmp=(1,2,3,4,5,6);
print "@tmp\n";
$#a-=2;
print "@tmp\n";
$#a+=2;
print "@tmp\n";
$#a-=2;
print "@tmp\n";
$#a+=10;
print "@tmp\n";

#배열의 데이터 들을 저장
$tmpChar="@tmp";
print "Save in Char to TmpArr with BigQuotes > ", $tmpChar, "\n";
#배열의 길이를 저장
$tmpChar=@tmp;
print "Save in Char to TmpArr > ", $tmpChar, "\n";

#내가 원하는 구분자를 넣어줌, 대박 좋음..
$tmpChar=join(":", @tmp);
print "$tmpChar\n";

$fileName="test.pl";

$name{123}="A";
$name{246}="B";
$name{349}="C";

$nameId{123}=1;
$nameId{246}=2;
$nameId{349}=3;

print "\n";

open(fileHandle, ">$fileName") || die "Can\'t open $fileName";
foreach(keys %name){ #키값들을 하나씩,, 123...246... 349
  $stud[0]=$_;
  $stud[1]=$name{$_};
  $stud[2]=$nameId{$_};
  $string=join(":",@stud);
  $string .="\n"; #이건머지
  #왜 저장되는 순서가 계속 바뀌지..
  print fileHandle $string;
}

close fileHandle;

open(fileHandle, "<$fileName") || die "Can\'t open $fileName";
#@allLines=<fileHandle>;
#print "@allLines";
@tmpArr;
while($aline=<fileHandle>){
  print "$aline";
  @tmpArr=(@tmpArr, split( /:/, $aline));
}

print "split > @tmpArr";

close fileHandle;
