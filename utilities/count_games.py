import os

if __name__ == '__main__':
    count = 0
    print(count)
    working_dir = os.getcwd()
    prefix = working_dir + "/generate_features/sgfs-by-date"
    for year in range(2005,2022):
        for month in range(1,13):
            
            if month < 10:
                month = f"0{month}"
            print(f"year {year} month {month} count {count}")
            
            for day in range (1,32):
                if day < 10:
                    day = f"0{day}"
                path = prefix + f"/{year}" + f"/{month}" + f"/{day}"
                if os.path.isdir(path):
                    filenames = os.listdir(path)
                    count += len(filenames)
    print(f"there are {count} files")

# Output:
# year 2005 month 01 count 0
# year 2005 month 02 count 0
# year 2005 month 03 count 0
# year 2005 month 04 count 0
# year 2005 month 05 count 0
# year 2005 month 06 count 0
# year 2005 month 07 count 0
# year 2005 month 08 count 0
# year 2005 month 09 count 0
# year 2005 month 10 count 0
# year 2005 month 11 count 0
# year 2005 month 12 count 238
# year 2006 month 01 count 395
# year 2006 month 02 count 549
# year 2006 month 03 count 676
# year 2006 month 04 count 1053
# year 2006 month 05 count 1557
# year 2006 month 06 count 2064
# year 2006 month 07 count 2667
# year 2006 month 08 count 3289
# year 2006 month 09 count 4222
# year 2006 month 10 count 4930
# year 2006 month 11 count 6362
# year 2006 month 12 count 7634
# year 2007 month 01 count 10174
# year 2007 month 02 count 12903
# year 2007 month 03 count 18134
# year 2007 month 04 count 21982
# year 2007 month 05 count 25836
# year 2007 month 06 count 29358
# year 2007 month 07 count 33839
# year 2007 month 08 count 39170
# year 2007 month 09 count 45485
# year 2007 month 10 count 50139
# year 2007 month 11 count 54740
# year 2007 month 12 count 59824
# year 2008 month 01 count 64120
# year 2008 month 02 count 68709
# year 2008 month 03 count 72605
# year 2008 month 04 count 77136
# year 2008 month 05 count 81084
# year 2008 month 06 count 85535
# year 2008 month 07 count 90880
# year 2008 month 08 count 94807
# year 2008 month 09 count 98354
# year 2008 month 10 count 103654
# year 2008 month 11 count 107815
# year 2008 month 12 count 111500
# year 2009 month 01 count 115476
# year 2009 month 02 count 120256
# year 2009 month 03 count 125981
# year 2009 month 04 count 129955
# year 2009 month 05 count 133312
# year 2009 month 06 count 137322
# year 2009 month 07 count 141271
# year 2009 month 08 count 146935
# year 2009 month 09 count 151817
# year 2009 month 10 count 156870
# year 2009 month 11 count 162631
# year 2009 month 12 count 166846
# year 2010 month 01 count 172130
# year 2010 month 02 count 176826
# year 2010 month 03 count 181313
# year 2010 month 04 count 186294
# year 2010 month 05 count 191146
# year 2010 month 06 count 196039
# year 2010 month 07 count 200023
# year 2010 month 08 count 204300
# year 2010 month 09 count 209218
# year 2010 month 10 count 214281
# year 2010 month 11 count 218702
# year 2010 month 12 count 221680
# year 2011 month 01 count 227558
# year 2011 month 02 count 232561
# year 2011 month 03 count 237043
# year 2011 month 04 count 241323
# year 2011 month 05 count 247494
# year 2011 month 06 count 252528
# year 2011 month 07 count 257601
# year 2011 month 08 count 262547
# year 2011 month 09 count 267934
# year 2011 month 10 count 274677
# year 2011 month 11 count 281215
# year 2011 month 12 count 286366
# year 2012 month 01 count 291464
# year 2012 month 02 count 297700
# year 2012 month 03 count 303277
# year 2012 month 04 count 307394
# year 2012 month 05 count 312152
# year 2012 month 06 count 317370
# year 2012 month 07 count 321671
# year 2012 month 08 count 327936
# year 2012 month 09 count 333439
# year 2012 month 10 count 338383
# year 2012 month 11 count 344940
# year 2012 month 12 count 349768
# year 2013 month 01 count 357446
# year 2013 month 02 count 363991
# year 2013 month 03 count 368649
# year 2013 month 04 count 372397
# year 2013 month 05 count 378627
# year 2013 month 06 count 383537
# year 2013 month 07 count 387741
# year 2013 month 08 count 394117
# year 2013 month 09 count 398326
# year 2013 month 10 count 402905
# year 2013 month 11 count 416491
# year 2013 month 12 count 427978
# year 2014 month 01 count 443361
# year 2014 month 02 count 461894
# year 2014 month 03 count 484908
# year 2014 month 04 count 508725
# year 2014 month 05 count 541529
# year 2014 month 06 count 578817
# year 2014 month 07 count 625350
# year 2014 month 08 count 687561
# year 2014 month 09 count 756380
# year 2014 month 10 count 827799
# year 2014 month 11 count 919356
# year 2014 month 12 count 1026713
# year 2015 month 01 count 1147698
# year 2015 month 02 count 1276643
# year 2015 month 03 count 1410003
# year 2015 month 04 count 1550849
# year 2015 month 05 count 1682817
# year 2015 month 06 count 1819181
# year 2015 month 07 count 1968917
# year 2015 month 08 count 2132108
# year 2015 month 09 count 2290082
# year 2015 month 10 count 2450234
# year 2015 month 11 count 2617587
# year 2015 month 12 count 2795819
# year 2016 month 01 count 2979930
# year 2016 month 02 count 3189229
# year 2016 month 03 count 3408156
# year 2016 month 04 count 3868251
# year 2016 month 05 count 4203472
# year 2016 month 06 count 4474169
# year 2016 month 07 count 4705748
# year 2016 month 08 count 4919292
# year 2016 month 09 count 5130646
# year 2016 month 10 count 5344349
# year 2016 month 11 count 5553514
# year 2016 month 12 count 5770750
# year 2017 month 01 count 5997506
# year 2017 month 02 count 6252569
# year 2017 month 03 count 6452307
# year 2017 month 04 count 6669382
# year 2017 month 05 count 6900308
# year 2017 month 06 count 7156954
# year 2017 month 07 count 7400289
# year 2017 month 08 count 7626126
# year 2017 month 09 count 7846147
# year 2017 month 10 count 8054432
# year 2017 month 11 count 8282185
# year 2017 month 12 count 8507164
# year 2018 month 01 count 8746284
# year 2018 month 02 count 9024594
# year 2018 month 03 count 9282891
# year 2018 month 04 count 9589617
# year 2018 month 05 count 9880396
# year 2018 month 06 count 10174433
# year 2018 month 07 count 10435519
# year 2018 month 08 count 10713223
# year 2018 month 09 count 10995552
# year 2018 month 10 count 11297303
# year 2018 month 11 count 11618783
# year 2018 month 12 count 11925021
# year 2019 month 01 count 12239717
# year 2019 month 02 count 12555752
# year 2019 month 03 count 12852275
# year 2019 month 04 count 13175485
# year 2019 month 05 count 13491957
# year 2019 month 06 count 13803593
# year 2019 month 07 count 14096412
# year 2019 month 08 count 14420519
# year 2019 month 09 count 14729166
# year 2019 month 10 count 15003008
# year 2019 month 11 count 15314287
# year 2019 month 12 count 15642876
# year 2020 month 01 count 16008152
# year 2020 month 02 count 16360436
# year 2020 month 03 count 16695126
# year 2020 month 04 count 17142490
# year 2020 month 05 count 17681105
# year 2020 month 06 count 18221408
# year 2020 month 07 count 18728669
# year 2020 month 08 count 19238906
# year 2020 month 09 count 19776333
# year 2020 month 10 count 20271370
# year 2020 month 11 count 20779163
# year 2020 month 12 count 21342340
# year 2021 month 01 count 21984674
# year 2021 month 02 count 22662697
# year 2021 month 03 count 23302454
# year 2021 month 04 count 23958244
# year 2021 month 05 count 24572015
# year 2021 month 06 count 25163828
# year 2021 month 07 count 25733778
# year 2021 month 08 count 26346043
# year 2021 month 09 count 26936218
# year 2021 month 10 count 26936321
# year 2021 month 11 count 26936330
# year 2021 month 12 count 26936330
# there are 26936330 files