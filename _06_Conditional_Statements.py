# Statements
    #   ==
    #   !=
    #   > , >=
    #   < , <=
    #   and
    #   or
    #   in
    #   not in


family = ['Haseeb', 'Emran', 'Mouyed']
if( ('Mouyed' in family) and ('Ahmad' not in family) or (len(family) == 5) ):
    print('Yoho, We are here')
else:
    print('Miss you guys')


print('########## if-elif-else ##########')
if family[0] == 'haseeb':
    print('iam Haseeb')
elif family[1].lower() == 'Emran':
    print('iam Emran')
elif family[2] == 'Mouyed':
    print('Iam mouyed')
else:
    print('iam not part of this family :(')
