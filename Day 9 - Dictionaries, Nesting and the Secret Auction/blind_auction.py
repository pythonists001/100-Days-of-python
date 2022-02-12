from replit import clear
from art import logo

# HINT: You can call clear() to clear the output in the console.
clear()
bidder_available = True
blind_auction = {}
max_bidding = 0
max_bidder_name = ""
print(logo)
while bidder_available:
    bidder_name = input("Enter your name : ").capitalize()
    bid_price = int(input("Enter your bid price : $"))
    blind_auction[bidder_name] = bid_price
    are_bidders_available = input("Are any more bidders available? Type 'Y' or 'N' ").upper()
    if are_bidders_available == "N":
        bidder_available = False
    clear()

for bidding in blind_auction:
    if blind_auction[bidding] > max_bidding:
        max_bidder_name = bidding
        max_bidding = blind_auction[bidding]
print(f"{max_bidder_name} has put the highest bid of ${max_bidding}")
