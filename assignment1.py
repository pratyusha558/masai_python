import subprocess

#TASK `1`:
t = ("a","b","c","d","e")
try:
  for i in t:
    print(i)
  t[0] = "e"
except Exception as e:
  print("Tuples can't be modified")

#TASK `2`:

st_python_pass= {2,4,1,7,9}
st_sql_pass = {1,3,4,2,5}
print(st_python_pass | st_sql_pass)
print(st_python_pass & st_sql_pass)
print(st_python_pass - st_sql_pass)

#TASK `3`:

ascii_lst = [65,66,67,68,69]
for i in ascii_lst:
  print(chr(i))
print(ord('Z'))

#TASK `4`:
result  = subprocess.run(['whoami'], shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(result.stdout)

