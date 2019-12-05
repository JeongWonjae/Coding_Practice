use threads;

$thr=threads->create(\&test);

sub test{
  sleep(2);
  print "in the tread\n";
}

print "go to sleep 5sec\n";
for(0..4){
  print "now : $_ sec\n";
  sleep(1);
}
