v7=35
v8=65
v9=285
v10=1900
v3_=1.5
v4_=80
p89=0.47
p910=0.342
p910_=0.37


profit89=p89*(v9-v7)+v7-2*v8-v3_
profit910=p910*(v10-v8)+v8-2*v9-v4_
profit910_=p910_*(v10-v8)+v8-2*v9-2*v7-v4_

print(profit89,profit910,profit910_)