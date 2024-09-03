class BiddingSystem:
    def __init__(self):
        self.bids = {}

    def place_bid(self, name, amount):
        self.bids[name] = amount
        print(f"Bid placed by {name} for ${amount}")

    def find_highest_bidder(self):
        highest_bidder = max(self.bids, key=self.bids.get)
        highest_bid = self.bids[highest_bidder]
        print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}")
        return highest_bidder, highest_bid

# Example usage
bidding_system = BiddingSystem()
bidding_system.place_bid("Alice", 100)
bidding_system.place_bid("Bob", 150)
bidding_system.place_bid("Charlie", 120)

bidding_system.find_highest_bidder()
