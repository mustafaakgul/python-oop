while(1):
    print('Çekmek istediğiniz tutarı giriniz')
    tutar = input()
    tutar = int(tutar)


    if (tutar%5 == 0):
        print("Ödemeni yapılıyor. Paranızı alınız:")
        if int(tutar/50):
            kuput_50 = int(tutar/50);
            print("kuput_50", kuput_50)
            if int((tutar - kuput_50*50)/20):
                kuput_20 = int((tutar - kuput_50*50) / 20);
                print("kuput_20", kuput_20)
                if int((tutar - kuput_50*50 - kuput_20 * 20) / 10):
                    kuput_10 = int((tutar - kuput_50*50 - kuput_20 * 20) / 10);
                    print("kuput_10", kuput_10)
                    if int((tutar - kuput_50 * 50 - kuput_20 * 20 - kuput_10 * 10) / 5):
                        kuput_5 = int((tutar - kuput_50 * 50 - kuput_20 * 20 - kuput_10 * 10) / 5);
                        print("kuput_5", kuput_5)

        elif int(tutar/20):
            kuput_20 = int(tutar / 20);
            print("kuput_20", kuput_20)
            if int((tutar - kuput_20*20)/10):
                kuput_10 = int((tutar - kuput_20*20) / 10);
                print("kuput_10", kuput_10)
                if int((tutar - kuput_20*20 - kuput_10 * 10) / 5):
                    kuput_5 = int((tutar - kuput_20*20 - kuput_10 * 10) / 5);
                    print("kuput_5", kuput_5)
        elif int(tutar / 10):
            kuput_10 = int(tutar / 10);
            print("kuput_10", kuput_10)
            if int((tutar - kuput_10*10)/5):
                kuput_5 = int((tutar - kuput_10*10) / 5);
                print("kuput_5", kuput_5)
        elif int(tutar/5):
            kuput_5 = int(tutar / 5);
            print("kuput_5", kuput_5)
    else:
        print("Sadece 5 in katı tutarlarda para çekeblirsiniz")