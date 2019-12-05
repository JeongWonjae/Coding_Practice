#펄에서 프로그램을 실행시킬 수 있음
#open 함수나 역따옴표로

#파일이름 맨앞이나 맨뒤에 '|' 파이프가 붙으면 명령어로 프로그램을 실행시킴
my $pid=open(FH, "| perl") || die "Writing failed:$!"; #my변수는 블록의 시점이 끝날때까지만 존재
print $!, "\n";
print "PID : $pid\n";
#펄 명령이후 해당 문자열을 출력시킴
print FH qq!print "Hello\\n";!; #qq!랑 원 표시 두개랑 마지막 ;! 는 뭘까?
close FH;
