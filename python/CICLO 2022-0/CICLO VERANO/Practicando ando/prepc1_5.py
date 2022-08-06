v = int(input("Ingrese un número: "))
if v < 0:
    print("Es tramposo")
elif v %3==0 and not v%6==0:
    print("Es tramposo")
elif v > 0 and v>= 100 and v%10 ==1:
    print("Es tramposo")
else:
    print("No es tramposo")
