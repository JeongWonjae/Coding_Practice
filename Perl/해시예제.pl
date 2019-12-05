$stufile="stufile.pl";
$scorefile="scoresfile.pl";

$maxnamelength=0;
$maxexamno=0;

open(fileHandle, "<$stufile") || die "Can\'t not open $stufile\n";

while(<fileHandle>){
  chop;
  ($stuid, $name, $year)=split(":", $_); #콜론으로 구분해서 저장
  $students{$stuid}=$name; #students 해시배열에 아이디와 이름을 저장
  $stuyear{$stuid}=$year; #stuyear 해시배열에 아이디와 학년을 저장
  if($maxnamelength<length($name)){
    $maxnamelength=length($name); #가장 긴 이름에 맞춤
  }
}

close fileHandle;

open(fileHandle, "<$scorefile") || die "Can\'t not open $scorefile\n";

while(<fileHandle>){
  chop;
  ($stuid, $examno, $score)=split(" ", $_); #공백으로 구분해서 각각 저장
  $scores{$stuid, $examno}=$score; #scores 해시배열에 아이디, 학과번호와 값으로 점수를 저장
  if($maxexamno<$examno){
    $maxexamno=$examno; #학과시험이 몇개인지 샘
  }
}
close fileHandle;

printf( "%3s %-${maxnamelenth}s %4s", "ID", "Name", "year");
# {} 로 둘러싼 이유는 뒤에 s라는 문자를 쓰기 위함
foreach(1..$maxexamno){
  printf("%4d", $_); #1부터 학과번호만큼 나열함
}
printf("%10s\n\n", 'Totals'); #토탈 문자 출력

foreach $stuid(sort (keys %students)){ #위 형식에 맞추어서 students 해시배열에서 id, name, year 값을 출력
  printf("%3d %-${maxnamelenth}s %4d", $stuid, $students{$stuid}, $stuyear{$stuid});
  $total=0;
  foreach $examno(1..$maxexamno){ #학과번호에 맞게 점수를 빼옴
    printf("%4d", $scores{$stuid, $examno});
    $total +=$scores{$stuid, $examno}; #토탈을 구해놓음
    $examtotal{$examno}+=$scores{$stuid, $examno}; #학과시험 번호를 구분으로 토탈값을 저장
  }
  printf("%10d\n", $total); #토탈 출력
}

printf( "%3s %-${maxnamelength}s %4s", '', "Total", '' );
$total = 0;
foreach $examno (1..$maxexamno) # 1..2..3
{
  printf( "%4d", $examtotal{ $examno } ); #학과시험마다 토탈점수
  $total += $examtotal{ $examno };
}
printf( "%10d\n\n", $total ); #총 점수
