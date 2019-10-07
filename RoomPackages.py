class roomPackages:
    def _init_(self, rooms, amenities):
        self.rooms = rooms
        self.amenities = amenities

        self.room_types = {'1. Standard, w/Full size Bed': 10,
                           '2. Standard for two, w/ two Full size beds': 20,
                           '3. Deluxe, w/Queen bed': 30,
                           '4. Premiere, w/ King bed': 40,
                           '5. Paradise Honeymoon Suite, w/ California King Bed and Jacuzzi Bath': 50,
                           '6. Paradise Master Suite, w/ California King Bed, Balcony w/ HotTub': 60
                           '7. Paradise Presidential Suite, w/ Balcony and Infinity Pool': 70}
        
        self.room_price = {'1. Standard, w/Full size Bed': $85
                           '2. Standard for two, w/ two Full size beds': $100,
                           '3. Deluxe, w/Queen bed': $125,
                           '4. Premiere, w/ King bed': $175,
                           '5. Paradise Honeymoon Suite, w/ California King Bed, and Jacuzzi Bath': $225,
                           '6. Paradise Master Suite, w/ California King Bed, Balcony w/ HotTub and Butler Services': $300
                           '7. Paradise Presidential Suite, w/ Balcony, Infinity Pool and Butler Services': $500}
