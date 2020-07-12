import yagmail #yagmail module is only available for pyhton2, it won't run in python3

contents = ['this is a trail mail from yagmail', '/home/shabarish/Desktop/document.pdf']

yagmail.SMTP('from@gmail.com').send('to@gmail.com', 'subject', contents)																																																																																																																																																																																					