file_name = 'proba.txt'
file = open(file_name, mode='w', encoding= 'utf8')
file_content = ("My soul is dark - Oh! quickly string,\nThe harp I yet can brook to hear;\nAnd let thy gentle"
                " fingers fling\nIts melting murmurs o'er mine ear.\nIf in this heart a hope be dear,\nThat sound"
                " shall charm it forth again:\nIf in these eyes there lurk a tear,\nTwill flow, and cease to burn my"
                " brain.\nBut bid the strain be wild and deep,\nNor let thy notes of joy be first:\nI tell thee,"
                " minstrel, I must weep,\nOr else this heavy heart will burst;\nFor it hath been by sorrow nursed,\nAnd"
                " ached in sleepless silence, long;\nAnd now 'tis doomed to know the worst,\nAnd break at once"
                " - or yield to song.")
file.write(file_content)
file.close()

file = open(file_name, mode='r')
file_content1 = file.read()
file.close()
print(file_content1)
