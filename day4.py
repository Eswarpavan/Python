"""strings"""
#sequence of character
#string ends with "\0"
# #initialization
# h="hello"
#stings are immutable objects
# ls1=[1,2,3,4]
# ls2=[5,6,7,8]
# print(ls1+ls2)
# string="Hello Everyone"
# char="H"
# print(string.find(char))
#print(string.rfind(char)) ---> rfind for reverse
# print(string.rfind(char))
# s="Eswar Pavan"
# print(s)
# print(s.upper())
# print(s.lower())
# print(s.capitalize())

"""dictionary"""
d={"name":"EswarPavan","followers":15800,"platform":"YouTube"}

"""
keys: name, followers, platform
value:EswarPavan, 15800, YouTube
"""
# for i in d.keys():
#     print(d[i])

# print(d)
# print(d.keys())
# print(d.values())
# print(d["name"])
# print(d["platform"])

# d1={"name":"EswarPavan","followers":15800,"platform":"YouTube","name":"Eswar"}
# print(d1.keys())
# print(d1.values())
d={"name":["EswarPavan","Eswar"],"followers":15800,"platform":"YouTube",23:{"age":23}}
#print(d.values())

# print(d[23]['age'])
# d["sports"]="cricket"
# print(d.items())

# d.update({"hobby":"Painting"})
# print(d)

del d["name"][1]
print(d)