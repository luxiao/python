def main():
  path="\\\\aiash-prod\\Dashboard\\DailyDownload\\2013_java\\201305\\MTD\\MNG_MTD_20130430_after_true_up.csv"
  input=open(path)
  output=open("text.csv",'w')
  for line in input.readlines():
    output.write(line)
  input.close()
  output.close()
  luxiao='a'
  print 
if __name__=='__main__':
  main()
