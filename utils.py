import datetime



def create_sub(y,title=""):
    ts=title+datetime.datetime.now().strftime("%m-%d_%I-%M")+".csv"
    outfile=open(ts,"w")
    outfile.write("ImageId,Label\r\n")
    for n,i in enumerate(y,1):
        outfile.write("{},{}\r\n".format(n,i))
    outfile.close()
