import random
import string
import datetime
import csv

numOfClients = 1000
numOfPromoters = 1000
numOfUsers = numOfClients + numOfPromoters
numOfEmailTokens = 1000

def generateRandomString(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

# CLIENT
def generateUsername():
    return generateRandomString(10)

def generateDateOfBirth():
    return datetime.date(random.randint(1950,2022), random.randint(1,12), random.randint(1,28))

def generateEmail():
    domenTypes = ["@gmail.com", "@wp.pl", "@kio.pl"]
    return generateRandomString(5) + domenTypes[random.randint(0, len(domenTypes) - 1)]

def generateEnabled():
    return random.randint(0, 1)

def generateLocked():
    return random.randint(0, 1)

def generateStaticUserId():
    return 1

def generateFavoriteMusic():
    musicTypes = ["jazz", "rock", "pop", "grunge", "metal", "blues", "electronic", "classic", "instrumental", "neosoul"]

    return musicTypes[random.randint(0, len(musicTypes) - 1)]

def generateFavoriteEventType():
    eventTypes = ["wedding", "halloween", "party 16+", "party 18+", "dance party", "costium party", "pijama party"]

    return eventTypes[random.randint(0, len(eventTypes) - 1)]

def generateRegistrationDate():
    return datetime.date(random.randint(2010,2022), random.randint(1,12), random.randint(1,28))

# PROMOTER
def generateTotalProvisionEarned():
    return random.randint(1000, 10000)

def generateEmploymentDate():
    return datetime.date(random.randint(2010,2022), random.randint(1,12), random.randint(1,28))

def generateTotalTicketsSold():
    return random.randint(10, 1000)

# EMAIL CONFIRMATION TOKEN
def generateCreationDate():
    return datetime.date(random.randint(2010,2022), random.randint(1,12), random.randint(1,28))

def generateConfirmationDate():
    return datetime.date(random.randint(2010,2022), random.randint(1,12), random.randint(1,28))

def generateExpirationDate():
    return datetime.date(random.randint(2010,2022), random.randint(1,12), random.randint(1,28))

def generateToken():
    return generateRandomString(32)

def generateUserId():
    return random.randint(1, numOfUsers)

def generateStaticEmailConfirmationTokenId():
    return 1

# ENTITIES GENERATION
def generateClient():
    return [generateUsername(), generateDateOfBirth(), generateEmail(), generateEnabled(), generateLocked(),
            generateStaticUserId(), generateFavoriteMusic(), generateFavoriteEventType(), generateRegistrationDate()]

def generatePromoter():
    return [generateUsername(), generateDateOfBirth(), generateEmail(), generateEnabled(), generateLocked(),
            generateStaticUserId(), generateTotalProvisionEarned(), generateEmploymentDate(), generateTotalTicketsSold()]

def generateEmailConfirmationToken():
    return [generateCreationDate(), generateConfirmationDate(), generateExpirationDate(), generateToken(),
            generateUserId(), generateStaticEmailConfirmationTokenId()]

# WRITE DATA TO CSV
with open('client.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['username', 'dateOfBirth', 'email', 'enabled', 'locked', 'staticUserId', 'favoriteMusic',
                     'favoriteEventType', 'registrationDate'])
    for n in range(numOfClients):
        writer.writerow(generateClient())

with open('promoter.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['username', 'dateOfBirth', 'email', 'enabled', 'locked', 'staticUserId', 'totalProvisionEarned',
                     'employmentDate', 'totalTicketsSold'])
    for n in range(numOfPromoters):
        writer.writerow(generatePromoter())

with open('emailConfirmationToken.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['creationDate', 'confirmationDate', 'expirationDate', 'token', 'userId', 'staticEmailConfirmationTokenId'])
    for n in range(numOfEmailTokens):
        writer.writerow(generateEmailConfirmationToken())