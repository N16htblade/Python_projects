import os
from art import logo

cls = lambda: os.system('cls')
cls()
print (logo)


continue_bidding = "yes"
participants = {}
winner_name = ""
winner_bid = 0

while continue_bidding == "yes":
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    participants[name] = int(bid)
    continue_bidding = input("Are there other participants? yes / no: ")
    cls = lambda: os.system('cls')
    cls()

for bidder in participants:
    if participants[bidder] > winner_bid:
        winner_name = bidder
        winner_bid = participants[bidder]
    else:
        pass

print (f"The winning bid was placed by {winner_name} with a bid of ${winner_bid}!")