from replit import clear
from art import logo

# HINT: You can call clear() to clear the output in the console.
clear()
bidder_available = True
blind_auction = {}

print(logo)


def find_highest_bidder(bids):
    max_bidding = 0
    max_bidder_name = ""

    for bidders in bids:
        if bids[bidders] > max_bidding:
            max_bidder_name = bidders
            max_bidding = bids[bidders]
    clear()
    print(logo)
    print(f"{max_bidder_name} is the winner with the bid amount of ${max_bidding}")


while bidder_available:
    clear()
    print(logo)
    bidder_name = input("Enter your name : ").capitalize()
    bid_price = int(input("Enter your bid price : $"))
    blind_auction[bidder_name] = bid_price
    are_bidders_available = input("Are any more bidders available? Type 'Y' or 'N' ").upper()
    if are_bidders_available == "N":
        bidder_available = False
        find_highest_bidder(blind_auction)
