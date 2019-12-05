#파일다루기

$fileName="test.pl";

if (-d $fileName){ die "$fileName is a directory."};

#파일이 존재하는가
-e $fileName || "$fileName is not exist.\n";
#파일이 텍스트 파일인가
-T $fileName || "$fileNmae is not a text file.\n";

#파일을 열어주는 핸들러 호출
open(fileHandle, $fileName) || die "Cannot open $fileName.\n";
@allLines=<fileHandle>;
print @allLines;
close(fileHandle);

#마지막 라인 쓰기모드로 실행
open(fileHandle, ">>$fileName") || die "Cannot open $fileName.\n";
#글 추가
print fileHandle << "end";
this line is add line.
end
close(fileHandle);

open(fileHandle, $fileName) || die "Cannot open $fileName.\n";
while( $aLine=<fileHandle>){
  print $aLine;
}
close(fileHandle);
