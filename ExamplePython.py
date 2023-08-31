def test_password(x):
    print(x)


a = "String 1"
b = "String 2"
print ("a =" + a + " and b=" + b)

x = "String 3"
y = "String 4"
print (f"x = {x} and y = {y}")

print ("c = {c} and d = {d}".format(c=1, d=2))

job_list = {'James F Mack': 'REDACTED', "Mary A North": 'Commander_A21', 'Timothy I C King': 'Clock_Repairman_E67'}

for name, job in job_list.items():
    print(f"{name} is a {job}")

Password = 'SuperSecretAdminPass'
test_password(Password)