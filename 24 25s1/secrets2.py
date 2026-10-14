codes = ["mpasta2a", "3cmayoad", "8orhioar", "ow2niv3i"]
message = ["".join([code[i], code[-(1+i)]]) for i,code in enumerate(codes)]
print("".join(message))