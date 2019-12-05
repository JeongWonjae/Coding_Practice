opendir(dirHandle, ".") || die "Failed opening.\n";
@tmpArr=readdir(dirHandle);
closedir dirHandle;

print "@tmpArr"
