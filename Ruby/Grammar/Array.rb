#make array
animal=['bear', 'rabit', 'lion']
puts animal[0].capitalize

#print
for type in 0...animal.size
  puts animal[type].capitalize
end

#init array
brand=Array.new(10, 0)
for i in 0..brand.length
  print ("#{brand[i]}/")
end
# next line
puts

#length
puts brand.length
puts brand.size

#add value to array
brand=['samsung', 'lg', 'musinsa', 'covernat', 'thisisneverthat']
brand << 'critic'
brand.push('adidas')
brand.unshift('nike') #add at first
print brand; puts

#delete value in array
brand.shift(1) #front
print brand; puts
brand.pop(2) #back
print brand; puts

#sort
brand.sort! {|x,y| x<=>y}
print brand; puts