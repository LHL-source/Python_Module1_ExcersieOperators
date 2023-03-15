# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
#exercise 1:The language spoken the most in Switzerland is the same as in Spain.
spain_language ="Spanish"
isSpanish = "Spanish"
switzerland_language="German"
print(spain_language==isSpanish and switzerland_language==isSpanish)
#w?y

#exercise 2:The most prevalent religion in Switzerland is the same as in Spain.
spain_religion="Catholic"#50%
switzerland_religion="Catholic" #34%
print(spain_religion==switzerland_religion)#Truthy

#exercise 3:The name length of Spain's capital does not equal that of Switzerland.
spain_capitalName="Madrid"
switzerland_capitalName="Bern"
spain_capitalName_length = len(spain_capitalName)
switzerland_capitalName_length =len(switzerland_capitalName)
#print(spain_capitalName_length)#6
#print(switzerland_capitalName_length)#4
#w?y
capitalNameLength_isNotEqual= spain_capitalName_length == switzerland_capitalName_length
print(capitalNameLength_isNotEqual)#false
#w?y

#exercise 4:Switzerland's GDP is greater than Spain's GDP.
#spain GDP is 10.7 (2020), switserland 11,8(2020)
spain_gdp=float(10.7)
switzerland_gdp=float(11.8)
gdpCompare_SwitserlandSpain = switzerland_gdp > spain_gdp
print(gdpCompare_SwitserlandSpain)#true
#w?y

#exercise 5:The population growth is less than 1% in Switzerland and Spain.

spain_populationGrowth=float(0.12)#0,12% (2023)
switzerland_populationGrowth=float(0.64) #0,64%(2023)
oneGrowth= float(1.0)
populationGrowth_lessThanOne = (spain_populationGrowth < oneGrowth)  and (switzerland_populationGrowth < oneGrowth)
print(populationGrowth_lessThanOne)
#w?y

#exercise 6:At least one of the two countries has a population count of over 10 million.
spain_populationCount=47222613 #(2023)
switzerland_populationCount=8563760#(2023)
tenMillion =10000000
spain_hasOverTenMillion=spain_populationCount > tenMillion
#print(spain_hasOverTenMillion)#more than 10 million, truthy
#w? y
switzerland_hasOverTenMillion=switzerland_populationCount > tenMillion
#print(switzerland_hasOverTenMillion)#falsy
#w?y
oneOfTheTwo_hasPopulationCount_overTenMillion=spain_hasOverTenMillion or switzerland_hasOverTenMillion
print(oneOfTheTwo_hasPopulationCount_overTenMillion)#truthy w?y

#exercise 7:Exactly one of the two countries has a population count of over 10 million.
#dus: 1)niet beide over 10 million 2)EN 3)niet beide onder 10 million
#hieronder uitwerking ad1)niet 1 van beide over 10 million
noOneOverTenMillion =(spain_populationCount > tenMillion) and (switzerland_populationCount > tenMillion)#falsy
#print(noOneOverTenMillion)
#falsy w?
#hieronder uitwerking ad3)niet 1 van beide onder 10 million
noOneUnderTenMillion=(spain_populationCount < tenMillion) and (switzerland_populationCount < tenMillion)#falsy
#print(f"no one under 10 million {noOneUnderTenMillion}")#falsy
#w?y
exactOneOfTwo=(noOneOverTenMillion==True) and (noOneUnderTenMillion ==True)
print(exactOneOfTwo)#falsy
#w? y
 