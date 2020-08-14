name = input("Enter file:")
if len(name) < 1 : 
	name = "mbox-short.txt"
handle = open(name)

mail=dict()
for line in handle:
	if line.startswith('From '):
		words=line.split()
		mailid=words[1]
		mail[mailid]=mail.get(mailid, 0)+1

	else:
		continue

most_mailer=None
most_mails=None

for mailer,mails in mail.items():
	if most_mails is None or mails>most_mails:
		most_mails=mails
		most_mailer=mailer
print (most_mailer, most_mails)
#words=line.split()