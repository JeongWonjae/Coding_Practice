puts "hello world"
puts "hi"

=begin
description
=end

a=1;b=2;
c=3

i=0
while i<6
  puts "#{i}. Hello"
  i=i+1
end

for i in 0..5
  puts "#{i}. Hello. Ruby!"
end

=begin
puts 'Enter your id.'
id=gets.chomp()
if id=='justv95'
  puts "Hi #{id}"
else
  puts "Wrong ID"
end
=end

=begin
puts "Enter your name "
name=gets.chomp()
def greeting(userName)
  puts userName+" Welcome!"
end
greeting(name)
=end

#container
numbers=['one', 'two', 'three']
puts(numbers.class)
puts(numbers[1])
numbers[1]='owt'
puts(numbers)
print(numbers)