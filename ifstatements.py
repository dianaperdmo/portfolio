start='''you are walking your dog coco because she needs to pee but youre also
running late to work or this will be the 5th time being late and if it gets that
far you will be fired'''
print(start)
user_input = input('''type home to go home and change to your work clothes or
 type wait to keep walking your dog or type boss to call boss to quit job''' )
if user_input =="home":
    print('''you go home and your dog pees on the couch before you leave so now
    your couch is stained.''')
    print('''since you were running late you had to take the later
    bus in which you see your old teacher and she tells you of a new job
    opportunity in her company and offers you the job.The End''' )
if user_input =="wait":
    print('''you wait for your dog to do her business and somehow make it to
    work a minute early''')
    print('''you later get back home and spend the whole rest of the evening
    glad you didnt get fired.The End''')
if user_input =="boss":
    print('''you call your boss to tell him you quit and he informs you that he
    is only hard on you because youre his best worker and he offers you a
    promotion so you dont quit. type quit to turn down the promotion or type wow
    to take take it''')
if user_input =="quit":
    print(''' no sorry i am quiting.But later that day realize you really need
    a job to survive so you call back to get your job back but your old boss
    tells you NO!!''')
if user_input =="wow":
    print('''you are surprised and happily take the promotion and live happily
    ever after!''')
