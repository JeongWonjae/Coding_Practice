
$a="H A C K E R";
$len=(length $a)-1;
print "$len\n";

print "$a\n";

for(0..1) #두번 반복
{
	for(0..$len) #열번 반복
	{
		$s1=substr($a, 0, $_); #첨부터 _번째까지 출력
		$s2=substr($a, $_+1); #나머지 전부다 출력
		print "$s2$s1\n";
		sleep 1; 
	}
}
print "\n";