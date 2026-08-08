# d={
#     "name":"khushi",
#     "age":20,
#     "idols":["akshay kumar","kim taehyung"]
# }
# print(d)
# print(d['idols'])
# d["is_adult"]=True
# print(d)
# d["name"]="Khushi"
# print(d)

e={
    "name":"khushi",
    "age":20,
    "score":{
        "chem":80,
        "maths":90,
        "cao":70
    },
    "idols":["akshay kumar","kim taehyung"]
}

#print(e)
# print(list(e.keys()))
# print(len(e))
# print(e.values())
# print(e.items())
# print(e.get("na"),"no key found")
# f={1:2,3:5,7:9}
# e.update(f)# add new dict to older dict
# print(e)
# e.update({"city":"rohtak"})
# print(e)

d={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts and figures"]
}
print(d)

marks={}
x=int(input("enter phys marks:"))
marks.update({"phys":x})

x=int(input("enter maths marks:"))
marks.update({"maths":x})

x=int(input("enter chem marks:"))
marks.update({"chem":x})
print(marks)