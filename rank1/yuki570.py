print("\n".join([e[0]for e in sorted({"A":int(input()),"B":int(input()),"C":int(input())}.items(),key=lambda x:x[1])[::-1]]))
