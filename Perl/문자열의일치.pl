$tmp="This is test String";

# =~ 는 문자열에 찾고 싶은 문자가 있는지
# 찾을 단어를 따옴표도 되지만 /로 둘러쌈
if($tmp=~/est S/ ){
  print "est is exist.\n";
} else {
  print "not exist\n";
}

#정규식
# .(온점)은 한글자, *(별)은 와일드카드로
#문자의 길이에 상관없이 찾을 수 있음, 0또는 몇개
# +(더하기)는 1또는 몇개를 찾음
# ?(물음표)는 0또는 1개를 찾음

if($tmp=~/t*S/){ #test S
  print "wildcard on\n"
} else {
  print "wildcard not on\n"
}

if($tmp=~/t?S/i){ #test S, i는 대소문자 무시
  print "? is on\n"
} else {
  print "? isn't on\n"
}

if($tmp=~/t[eac]s/i){ #괄호안에 있으면 그 문자중에 하나만
#해당하면 true
  print "brackat is on\n";
} else {
  print "brackat isn't on\n";
}

$_="This is test String";
#만약 변수 선언이 안되어있으면 $_가 있는 것으로 봄
if( /test/i ){
  print "y\n";
} else {
  print "n\n"
}

#찾은 문자열의 앞부분과 뒷부분 출력
print "Front : [$`]\nBack : [$']\n";
