class DistanceConversion:
    def get_distance(self):
        self.distanecInKm=float(input("Enter the distance in km: "))
    def print_distance(self):
        distanecInM=self.distanecInKm*1000
        print(distanecInM)
d=DistanceConversion()
d.get_distance()
d.print_distance()


