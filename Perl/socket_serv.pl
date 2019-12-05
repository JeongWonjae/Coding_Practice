use strict;
use Socket;

my $port="7890";
my $proto=getprotobyname("tcp");

socket(SERVER, PF_INET, SOCK_STREAM, $proto) || die "socket : $!";
setsockopt(SERVER, SOL_SOCKET, SO_REUSEADDR, 1) || die "setsock : $!";

my $paddr=sockaddr_in($port, INADDR_ANY);

bind(SERVER, $paddr) || die "bind : $!";
listen(SERVER, SOMAXCONN) || die "listen : $!";
print "SERVER started on port $port";

my $client_addr;
while($client_addr=accept(CLIENT, SERVER)){
  my ($client_port, $client_ip) = sockaddr_in($client_addr);
	my $client_ipnum = inet_ntoa($client_ip);
	my $client_host = gethostbyaddr($client_ip, AF_INET);

	print "got a connection from: $client_host","[$client_ipnum] ";

	print CLIENT "Hello! from the server";
	close CLIENT;
}
