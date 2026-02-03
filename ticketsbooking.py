capacity = 350
remaining_seats = 350
total_bookings = 0
tickets_sold = 0
rejected_bookings = 0
while remaining_seats > 0:
   tickets = int(input("Enter number of tickets (0 to exit): "))
   if tickets == 0:
       break
   if tickets < 1 or tickets > 15:
       print("BOOKING REJECTED - Invalid ticket count")
       rejected_bookings += 1
       continue
   if tickets > remaining_seats:
       print("BOOKING REJECTED - Not enough seats")
       rejected_bookings += 1
       continue
   valid = True
   for i in range(tickets):
       age = int(input("Enter age: "))
       if age < 12:
           valid = False
           break
   if not valid:
       print("BOOKING REJECTED - Age restriction")
       rejected_bookings += 1
       continue
   print(f"BOOKING CONFIRMED - {tickets} tickets")
   total_bookings += 1
   tickets_sold += tickets
   remaining_seats -= tickets
   if remaining_seats == 0:
       break
print("Final Report:")
print("Total Bookings:", total_bookings)
print("Total Tickets Sold:", tickets_sold)
print("Rejected Bookings:", rejected_bookings)
print("Remaining Seats:", remaining_seats)
