st="mp poLytechnic"
print(st)
print(type(st))
print(st.upper())
print(st.lower())
print(st.title())
print(st.capitalize())
print(st.swapcase())
print(len(st))
print(st.count('c'))
print(st.endswith('c'))
fl=input("enter the name of your friends")
print(fl)
d=fl.split(',')
for i in d:
    print(i)


# name=input("enter your name")
# if name.isalpha():
#     print(name)
# else:
#     print("You have not entered correct name")

# age=input("enter your age")
# if age.isdigit():
#     print(age)
# else:
#     print("You have not entered correct age")


# enroll=input("enter your enrollment no ")
# if enroll.isalnum():
#     print(enroll)
# else:
#     print("You have not entered correct enroll")



# name=input("enter your name")
# print(name)
# print(name.strip('!'))
# print(name.lstrip())
# print(name.rstrip())

# st2="her name is tamanna and tamanna is good girl."
# print(st2.replace('tamanna','sonia'))
para="On the Insert tab, the galleries include items that are designed to coordinate with the overall look of your document. You can use these galleries to insert tables, headers, footers, lists, cover pages, and other document building blocks. When you create pictures, charts, or diagrams, they also coordinate with your current document look."
print(para.replace('the','that'))


str3="her name is tamanna and tamanna is good girl"
search="tamanna"
print(str3.find(search))
rep="Sonia"
if str3.find(search):
    print(str3.replace(search,rep))

print(str3.index(search))