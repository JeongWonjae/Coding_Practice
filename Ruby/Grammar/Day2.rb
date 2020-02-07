
=begin
def h(name="world")
  puts "hello #{name.capitalize}!"
end

h"wonjae"
h
h()
=end

=begin : call class
class Greeter
  def initialize(name="world")
    @name=name
  end

  def sayHi
    puts "Hi #{@name}!"
  end

  def sayBye
    puts "Bye #{@name}, come back plz."
  end
end

g=Greeter.new("wonjae")
g.sayHi
g.sayBye


g2=Greeter.new("chulsu")
g2.sayHi
g2.sayBye

g3=Greeter.new()
g3.sayHi
g3.sayBye
=end

=begin
class Greeter
  def initialize(name="world")
    @name=name
  end

  def sayHi
    puts "Hi #{@name}!"
  end

  def sayBye
    puts "Bye #{@name}, come back plz."
  end

  attr_accessor :name
end

puts(Greeter.instance_methods(false))
# check 'sayHi' mothod if in exits in class
g=Greeter.new("wonjae")
puts(g.respond_to?("sayHi")) #true
puts(g.respond_to?("name")) #false

g2=Greeter.new("andy")
puts(g2.respond_to?("name"))
puts(g2.sayHi)
g2.name="berry"
puts(g2.sayHi)
=end

class MegaGreeter
  attr_accessor :names


  def initialize(names="world")
    @names=names
  end

  def sayHi
    if @names.nil?
      puts "..."
    elsif @names.respond_to?("each") # @names was respond by each object
      @names.each do |name|
        puts "Hello #{name}!"
      end
    else
      puts "Hello #{@names}!"
    end
  end

  def sayBye
    if @names.nil?
      puts "..."
    elsif @names.respond_to?("join")
      if @names.respond_to?("each")
        @names.each do |name|
          puts "Goodbye #{name}"
        end
      else
        puts "Goodbye #{@names.join(",")}. come back plz!"
      end
    else
      puts "Goodbye #{@names}. comeback plz"
    end
  end

end

def getValue()
  i=1; j=2; k=3;
  return i,j,k
end

#if this file is main
if __FILE__==$0
  g=MegaGreeter.new
  g.sayHi

  g.names="zeke"
  g.sayHi
  g.sayBye

  g.names=["brenda", "reona", "rulru", "amumu", "son"]
  g.sayHi
  g.sayBye

  g.names=nil
  g.sayHi

  #hash
  e={1=>'a', 2=>'b', 3=>'c'}
  puts e[1]
  print e[2]+"\n"
  p e[3]

  tmp="My name is wonjae"
  puts tmp=~/wonjae/
  puts tmp=~/chulsu/

  puts 'true' if tmp=~/is/

  tmpArr=getValue
  if tmpArr.respond_to?("each")
    tmpArr.each do |a|
      puts "values is #{a}"
    end
  end

  for index in 0...tmpArr.size
    puts tmpArr[index]
  end
end




