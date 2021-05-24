import os
import art


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


next_person = True
bids = {}
first_run = True
while next_person:
    if first_run:
        print(art.logo)
        print("Welcome in a Secret Auction Program")
        first_run = False
    name = input("Type a name of bidder ")
    if name in bids:
        print("There is someone with this name! Type different name or add surname")
    else:
        bid_price = input("Type a maximum bid price ")
        bids[name] = bid_price
        add_more = input("Type 'yes' if you want to add new person or 'no' if there is no more bidders ")
        while not (add_more == "no" or add_more == "yes"):
            add_more = input("Type 'yes' if you want to add new person or 'no' if there is no more bidders ")
        if add_more == "no":
            next_person = False
        cls()

highest_bid = 0
winner = "none"
for name in bids:
    if int(bids[name]) > highest_bid:
        highest_bid = int(bids[name])
        winner = name
print(f"Winner of auction is {winner} with {highest_bid}")
