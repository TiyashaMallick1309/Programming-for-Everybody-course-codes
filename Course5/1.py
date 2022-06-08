"""Write code that combines the following variables so that the sentence “You are doing a great job, keep it up!” is assigned to the variable message. Do not edit the values assigned to by, az, io, or qy."""

by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"
a=(by,az)
c=" ".join(a)
b=(c,io)
d="".join(b)
e=(d,qy)
message=", ".join(e)
print(message)
