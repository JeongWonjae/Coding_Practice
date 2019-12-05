use strict;
use Socket;

my $host="localhost";
my $port="7890";
my $proto=getprotobyname("tcp");

my $iaddr=inet_aton($host); #주소형식으로 변환시켜주는 함수
my $paddr=sockaddr_in($port, $iaddr);

socket(SOCKET, PF_INET, SOCK_STREAM, $proto) || die "Socket : $!"; # $!는 에러메시지를 담는 변수
connect(SOCKET, $paddr) || die "connect : $!";

my $line;
while($line=<SOCKET>){
  print $line;
}

close SOCKET or die "close : $!";
