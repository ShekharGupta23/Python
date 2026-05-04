s = 'My Profile: https://www.geeksforgeeks.org/404.html/ in the portal of https://www.geeksforgeeks.org/'
s1 = s.split()

res=[]
for i in s1:
    if i.find("https:")==0 or i.find("http:")==0:
        res.append(i)
print("Urls: ", res)