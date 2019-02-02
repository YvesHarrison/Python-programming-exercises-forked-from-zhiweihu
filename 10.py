def Question10():
   sen=input().split(" ")
   sen=list(set(sen))
   sen.sort()
   print(','.join(sen))

Question10()