#make hash
score={"math"=>80, "english"=>90, "science"=>75}
#or
score2=Hash.new
score2['math']=80
score2['english']=90
score2['science']=75

#print value using key
puts score['math']

#iterator
score.each{|sub, scr| puts "Subject : #{sub} \t Score : #{scr}"}