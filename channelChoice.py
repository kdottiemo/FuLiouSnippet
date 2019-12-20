def channelCheck(cosSolarZA, mbs):
    if(cosSolarZA <= 0.0001):
        mbn = mbs + 1
    else:
        mbn = 1

    # Make print statement more descriptive about 
    # channel selection below:
    print 'mbn = ', mbn



def main():
    mbs = 6                # Number sw bands

    # Cosine of the zenith angle (0-1):
    cosSolarZA = float(raw_input('Enter cos(ZA): '))

    print 'Calling channelCheck()...'
    
    channelCheck(cosSolarZA, mbs)



if __name__=='__main__':
    main()
