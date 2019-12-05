$filename="test.pl";
@aas={1,2,3,4,5};

open(fileHandle, ">>$filename");
$bas=join(":", @aas);
print "$bas\n";

$string=join(":",@stud);

print fileHandle $b;
close(fileHandle);

sub sub1{
  print "this is sub1\n";
}

sub sub2{
  print "this is sub2\n";
}

sub tempName{
  local($tn)="\n";
  local($temp);

  for('0000'...'9999'){
    $temp="tmp" ,$_, ".gr"; #랜덤한 이름을 만듬
    if(!(-d $temp) && !(-e $temp)){ #폴더내의 파일이름이 존재하는지, 디렉터리가 아닌지 확인
      $tn=$temp;
      last; #만족하면 끝냄
    }
  }
  return $tn;
}

1; #무언가 값을 리턴해야함
