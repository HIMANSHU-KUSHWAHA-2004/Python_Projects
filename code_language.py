message = str(input("ENTER THE MESSAGE : "))
words = message.split()
coding = int(input("ENTER 1 FOR CODING AND 2 FOR DECODING : "))
if coding == 1:
    newords = []
    for word in words:
        if len(word) >=3:
            tit = "bit" + word[1:] + word[0] + "gbx"
            newords.append(tit)
        else:
            newords.append(word[::-1])    
    coded_message = " ".join(newords)
    print(coded_message)
    """TIP AGER SAB THEEK LAG RHA HO FIR BHI SAHI RESULT NA AAYE THEN CHECK FOR INDENTATION ITS AN
    IMPORTANT PART OF PYTHON"""
    
elif coding == 2:
        newords = []
        for word in words:
            if len(word) >= 3:
                tit = word[-4] + word[3:-4]
                newords.append(tit)
            else:
                newords.append(word[::-1])
                # THIS IS TO REVERSE A STRING YOU CAN USE IT ITS COME UNDER SLICING
        decoded_message = " ".join(newords)
        print(decoded_message)            