class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")


emails = list()
line = input()

while line != 'Stop':
    line = line.split(' ')
    mail_sender = line[0]
    mail_receiver = line[1]
    mail_content = line[2]
    mail = Email(mail_sender, mail_receiver, mail_content)
    emails.append(mail)
    line = input()


indices = list(map(int, input().split(', ')))

for index in indices:
    emails[index].send()

for mail in emails:
    mail.get_info()
