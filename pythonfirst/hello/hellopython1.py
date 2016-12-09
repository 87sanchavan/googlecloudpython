
from google.cloud import bigquery
print(dir(bigquery))
t1 = locals()



d = {'x': 1, 'y': 2, 'z': 3}

for key, value in t1.items():
    print(key +":"+value)