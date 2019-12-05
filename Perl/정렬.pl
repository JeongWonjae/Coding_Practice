@array=("Ant", "Cat", "Dad", "Banana", "Fly", "Eye");
@sort_array=sort @array;
print "@sort_array\n";

#맨 앞 숫자 순서대로 정렬함
@number_array=(1, 24, 139, 32, 254, 2, 40);
@sort_number_array=sort @number_array;
print "@sort_number_array\n";

#배열의 각 요소가 a와 b에 대입되어짐
@sort_number_array=sort {$a <=> $b}@number_array;
print "@sort_number_array\n";

#-------------------------------------------
#긴 문자열 저장
$text=<<EOT;
index.html 354
sitemap.html 27
product.html 297
board.cgi 75
test.html 700
EOT

#공백제거
chomp($text);
#공백을 기준으로 나누어서 저장
@array=split(/\n/, $text);
#csort 함수로 이용해서 반환되는 값을 먼저 저장
@sort_array=sort{ &csort($b,$a)}@array;
print join("gg\n",@sort_array,'');

sub csort{
  my($ta, $tb)=@_;
  my($pa, $ca)=split / /, $ta;#공백을 기준으로 앞의 값은 pa 뒤에 값은 ca에 저장
  my($pb, $cb)=split / /, $tb;#즉 pa는 html파일 이름, ca는 카운터 숫자가 됨
  $ca <=> $cb; #비교한 값을 반환
}
