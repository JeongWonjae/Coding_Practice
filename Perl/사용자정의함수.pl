sub mysubroutine{
  print "hello world\n";
}

&mysubroutine;

#인수는 @_라는 특수한 배열로 전달됨
sub args{
  print "@_\n";
}

sub biargs{
  &args("hello", "there", "?");
  print "@_\n";
}
&biargs("hey", "hi");

#마지막으로 도출된 값을 리턴함
sub max2{
  if($_[0]>$_[1]){
    return $_[0];
  }
  $_[1];
}

$max=&max2(10, 5);
print "$max\n";

$max=&max2(7, 15);
print "$max\n";

#함수 밖에서의 변수들은 함수 안에서도 볼 수 있다. 즉 변경시킬수 있다.
#중요한 데이터 dum을 함수내에서 다시 정의해 중요한 데이터가 사라질 수 있음
#local이라는 범위변경자를 사용하여 변수를 지역화할 수 있음
$dum="this is very important data";

$max=&max(11, 5);
print "$max\n";

$max=&max(9, 14);
print "$max\n";

print "$dum\n";

sub max{ #local 변수 적용
  local($dum) = ($_[0]>$_[1]) ? $_[0] : $_[1];
}
