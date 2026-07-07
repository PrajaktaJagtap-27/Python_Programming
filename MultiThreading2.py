import threading

def Display():
    print("Inside display :",threading.get_ident())

def main():
    print("Inside main :",threading.get_ident())  #11

    tobj = threading.Thread(target=Display)   #update

    tobj.start()

if __name__ == "__main__":
    main()
