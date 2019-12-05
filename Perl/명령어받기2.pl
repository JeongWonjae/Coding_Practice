#Save received commands to : options
for(my $i=0;$i<=$#ARGV;$i++){
  if(@ARGV[$i]=~/-src/i){
    my $tmp_i=$i+1;
    $src=@ARGV[$tmp_i];
    print "src = $src\n";
  }
  if(@ARGV[$i]=~/-dst/i){
    my $tmp_i=$i+1;
    $src=@ARGV[$tmp_i];
    print "dst = $src\n";
  }
  if(@ARGV[$i]=~/-port/i){
    my $tmp_i=$i+1;
    $portNumber=@ARGV[$tmp_i];
    print "portN = $portNumber\n";
  }
}
#end



__END__
1.ACK 스캔
2.TCP HalfOpen 스캔
3.Fin 스캔
4.XMASS 스캔
5.NULL 스캔
