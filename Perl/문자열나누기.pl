#배열에 + 문자로 구분해서 저장
$tmp="This+is+test+String";
@tmpArr=split( /\+/, $tmp);

print("$tmp\n@tmpArr\n");
print("---------------\n");

@tmpArr2=(
  "A     test 75",
  "B     test 90",
  "C     test 100"
);

#각각 출력을 해봄
foreach(@tmpArr2){
  print;
  print "\n";
}

@temproraryArr;

foreach(@tmpArr2){
  #앞의 문자를 이용하여 분리하되 뒤에 +문자가 있으면 개수를무시하고
  #하나로 취급해서 분리함
  @temproraryArr=split(/ +/);
  #printf 함수는 형식문자열의 요구에 맞추어 출력
  #문자폭에 맞추어 출력할 때 오른쪽에 붙여서 출력하는데
  #이를 원치 않을경우 -를 붙힘
  printf("%-10s \n%-7s \n%3s\n",
        $temproraryArr[0], $temproraryArr[1], $temproraryArr[2]);
}

printf ("|%-15s|%04d|%10.3f|\n", "Thank you ", 50, 502.145);
