import art
print(art.logo)
# TODO-1: Ask the user for input
bidders={}
no_bid= False
while not no_bid:
    name= input("Name: ")
    bid_value= int(input("Place your bid: $ "))
# TODO-2: Save data into dictionary {name: price}
    bidders[name]= bid_value
    response= input("any other bidder s? Type yes or no: ")
# TODO-3: Whether if new bids need to be added
    if response.lower()=="yes":
        no_bid = False
        print("\n"*1000)
    else:
        no_bid = True
# TODO-4: Compare bids in dictionary
highest_bidder=max(bidders, key=bidders.get)
highest_bid= bidders[highest_bidder]
#
# for bidders,bid in bidders.items():
#     if int(bid) > highest_bid:
#         highest_bid= bid
#         highest_bidder= bidders
#
print(f"Highest bidder is {highest_bidder} for ${highest_bid}")


