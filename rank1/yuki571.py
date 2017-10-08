print("\n".join([e[0]for e in sorted({"A":[int(i)for i in input().split()],"B":[int(i)for i in input().split()],"C":[int(i)for i in input().split()]}.items(),key=lambda x:(x[1][0],-x[1][1]))[::-1]]))
