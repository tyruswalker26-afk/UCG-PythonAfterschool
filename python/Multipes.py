# program Desctiption: Checking multipleses of 5 from no.s 1-20

#Creating list called numbers

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 

#For loop to check numbers divisible by 5
for i in numbers:
    if i % 5 == 0:
        print(i)