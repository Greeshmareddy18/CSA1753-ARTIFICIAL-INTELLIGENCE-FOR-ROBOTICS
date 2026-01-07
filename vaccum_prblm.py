# Vacuum Cleaner Problem using Simple Reflex Agent

# Function to display environment state
def display_state(location, room_a, room_b):
    print("----------------------------------")
    print(f"Vacuum Location : Room {location}")
    print(f"Room A Status   : {room_a}")
    print(f"Room B Status   : {room_b}")
    print("----------------------------------\n")


# Vacuum cleaner agent logic
def vacuum_cleaner():
    
    # Initial Environment State
    location = 'A'          # Vacuum starts in Room A
    room_a = 'Dirty'
    room_b = 'Dirty'
    
    print("Initial Environment State")
    display_state(location, room_a, room_b)
    
    # Continue until both rooms are clean
    while room_a == 'Dirty' or room_b == 'Dirty':
        
        # If vacuum is in Room A
        if location == 'A':
            if room_a == 'Dirty':
                print("Action: SUCK (Cleaning Room A)")
                room_a = 'Clean'
            else:
                print("Action: MOVE RIGHT (Going to Room B)")
                location = 'B'
        
        # If vacuum is in Room B
        elif location == 'B':
            if room_b == 'Dirty':
                print("Action: SUCK (Cleaning Room B)")
                room_b = 'Clean'
            else:
                print("Action: MOVE LEFT (Going to Room A)")
                location = 'A'
        
        display_state(location, room_a, room_b)
    
    print("✅ Both rooms are CLEAN. Task completed!")


# ---------------- MAIN PROGRAM ----------------

print("Vacuum Cleaner Problem Simulation")
print("Using Simple Reflex Agent\n")

vacuum_cleaner()
