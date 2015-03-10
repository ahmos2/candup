#!/usr/bin/env python
import sys,pycanopen

args=sys.argv;
args.reverse() #reverse puts arg0 on the top
args.pop() # Skip own name

print "Input:",args[len(args)-1]
input=pycanopen.CANopen(args.pop())
outputs=[]

for arg in args:
    print "Output:",arg
    outputs.append(pycanopen.CANopen(arg))

#vcan0=pycanopen.CANopen('vcan0')
#vcan1=pycanopen.CANopen('vcan1')
while(True):
    frame=input.read_can_frame()
    
    for output in outputs:
        output.write_can_frame(frame)
    
#    vcan0.write_can_frame(frame)
#    vcan1.write_can_frame(frame)
