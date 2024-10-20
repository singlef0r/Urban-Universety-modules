recipient, sender = 'vasyok1337@gmail.com', 'urban.info@gmail.com'

if "@" not in recipient or "@" not in sender:
    print(1)

if "@" not in (recipient, sender):
    print(11)
