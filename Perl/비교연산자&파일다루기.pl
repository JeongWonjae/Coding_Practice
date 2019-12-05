@a=(1,2,3);
print  "@a";
print @a;
print "\n";

$big=100;
$small=1;

$tmp= $big<$small || ($ts=$small); #앞이 거짓이면 뒤를 실행함
print $ts, "\n";

if(big cmp small)
{
	print "different\n";
}

$fileName="test2.pl";

if(-d $fileName)
{
	die "$fileName is a directory.\n"  #메시지 출력 후 종료
}

-e $fileName || die "$fileName is not exist.\n";
-T $fileName || die "$fineName is not a text file.\n";

open(fileHandle, $fileName) || die "Connect open $fileName.\n";
@allLines=<fileHandle>;
print @allLines;

print "----------------------------------------------";

while($aLine=<fileHandle>) #왜 둘중하나만 되징..
{
	print "$aLine";
}

close(fileHandle);

