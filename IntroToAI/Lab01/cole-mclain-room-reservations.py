# Cole McLain Lab 01 
# Room reservation recommendations

class RoomReservation:
    @staticmethod
    def recommend_room(attendees : int, projector_needed : bool):
        """Prints a room recommendation to console based on # of attendees and if a projector is needed"""
        room : str = "N/A"
        
        # Print statements for readability 
        print("\n--- Meeting Room Reservation ---")
        print(f"Request: Atendees={attendees}, Projector Needed={projector_needed}")

        # Calculate the recommendation
        if 1 <= attendees <= 5:
            room = "Room Alpha (Small, No Projector)"
        elif attendees >= 6 and attendees <= 15:
            if projector_needed:
                room = "Room Beta (Medium, Has Projector)"
            else:
                room = "Room Gamma (Medium, No Projector)"
        elif attendees >= 16:
            room = "Reservation Denied (No large rooms available)"
        else:
            room = "Error Invalid number of attendees."
        
        # Finish printing
        print(f"Recommended Room {room}")
        print("---------------------------------")


# Test case 1: should return "Room Alpha (Small, No Projector)"
RoomReservation.recommend_room(4, False)

# Test case 2: should return "Room Beta (Medium, Has Projector)"
RoomReservation.recommend_room(12, True)

# Test case 3: should return "Reservation denied..."
RoomReservation.recommend_room(20, True)

# Test case 4: should return "Error Invalid number of attendees"
RoomReservation.recommend_room(-34, True)
