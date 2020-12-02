from brain import Brain

price = int(input("Requested Price: "))
SURVEY = "https://forms.gle/sQ2Mb66UBgcPw6J46"
automate = Brain(p=price, survey=SURVEY)
print(automate.get_soup())
