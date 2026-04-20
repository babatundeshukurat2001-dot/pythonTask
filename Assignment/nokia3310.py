import sys

while True:
    print("""
=====================================
          NOKIA 3310 MENU
=====================================
1. PhoneBook
2. Messages
3. Chat
4. Call Register
5. Tones
6. Settings
7. Call Divert
8. Games
9. Calculator
10. Reminder
11. Clock
12. Profiles
13. SIM Services

0. Exit
=====================================""")

    number = int(input("\nEnter your choice: "))

    if number == 1:          # PHONEBOOK
        print("""
PHONEBOOK
1. Search
2. Service No
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags
0. Back""")
        
        number = int(input("\nEnter choice: "))
        
        if number == 8:      # Options submenu
            print("""
OPTIONS
1. Type of view
2. Memory status""")
            number = int(input("\nEnter number from 1-2: "))
            if number == 1:
                print("Type of view")
            elif number == 2:
                print("Memory status")
        elif number == 1:
            print("Search")
        elif number == 2:
            print("Service No")
        elif number == 3:
            print("Add name")
        elif number == 9:
            print("Speed dials")
        elif number == 10:
            print("Voice tags")

    elif number == 2:        # MESSAGES
        print("""
MESSAGES
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10. Service command editor
0. Back""")
        
        number = int(input("\nEnter choice: "))
        
        if number == 7:      # Message settings
            print("""
MESSAGE SETTINGS
1. Set
2. Common""")
            number = int(input("\nEnter number from 1-2: "))
            
            if number == 1:
                print("""
SET
1. Message centre number
2. Message sent as
3. Message validity""")
                number = int(input("\nEnter number from 1-3: "))
                if number == 1:
                    print("Message centre number")
                elif number == 2:
                    print("Message sent as")
                elif number == 3:
                    print("Message validity")
            elif number == 2:
                print("""
COMMON
1. Delivery reports
2. Reply via same centre
3. Character support""")
                number = int(input("\nEnter number from 1-3: "))
                if number == 1:
                    print("Delivery reports")
                elif number == 2:
                    print("Reply via same centre")
                elif number == 3:
                    print("Character support")
        elif number == 1:
            print("Write messages")
        elif number == 2:
            print("Inbox")
        elif number == 3:
            print("Outbox")
        elif number == 4:
            print("Picture messages")
        elif number == 5:
            print("Templates")
        elif number == 6:
            print("Smileys")
        elif number == 8:
            print("Info service")
        elif number == 9:
            print("Voice mailbox number")
        elif number == 10:
            print("Service command editor")

    elif number == 3:
        print("\n>>> Chat opened\n")

    elif number == 4:        # CALL REGISTER
        print("""
CALL REGISTER
1. Missed calls
2. Received calls
3. Dialed numbers
4. Erase recent call lists
5. Show call duration
6. Show call cost
7. Call cost setting
8. Prepaid credit
0. Back""")
        
        number = int(input("\nEnter choice: "))
        
        if number == 5:
            print("Show call duration submenu (further options not expanded)")
        elif number == 6:
            print("Show call cost submenu")
        elif number == 7:
            print("Call cost setting submenu")
        elif number == 1:
            print("Missed calls")
        elif number == 2:
            print("Received calls")
        elif number == 3:
            print("Dialed numbers")
        elif number == 4:
            print("Erase recent call lists")
        elif number == 8:
            print("Prepaid credit")

    elif number == 5:        # TONES
        print("""
TONES
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and gaming tones
8. Vibrating alert
9. Screen saver""")
        
        number = int(input("\nEnter choice: "))
        if number == 1:
            print("Ringing tone")
        elif number == 2:
            print("Ringing volume")
        elif number == 3:
            print("Incoming call alert")
        elif number == 4:
            print("Composer")
        elif number == 5:
            print("Message alert tone")
        elif number == 6:
            print("Keypad tones")
        elif number == 7:
            print("Warning and gaming tones")
        elif number == 8:
            print("Vibrating alert")
        elif number == 9:
            print("Screen saver")

    elif number == 6:        # SETTINGS
        print("""
SETTINGS
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings""")
        
        number = int(input("\nEnter choice: "))
        
        if number == 1:
            print("Call settings submenu")
        elif number == 2:
            print("Phone settings submenu")
        elif number == 3:
            print("Security settings submenu")
        elif number == 4:
            print("Restore factory settings")

    elif number == 7:
        print("\n>>> Call Divert\n")
    elif number == 8:
        print("\n>>> Games\n")
    elif number == 9:
        print("\n>>> Calculator\n")
    elif number == 10:
        print("\n>>> Reminder\n")
    elif number == 11:       # CLOCK
        print("""
CLOCK
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time""")
        
        number = int(input("\nEnter choice: "))
        if number == 1:
            print("Alarm clock")
        elif number == 2:
            print("Clock settings")
        elif number == 3:
            print("Date setting")
        elif number == 4:
            print("Stopwatch")
        elif number == 5:
            print("Countdown timer")
        elif number == 6:
            print("Auto update of date and time")

    elif number == 12:
        print("\n>>> Profiles\n")
    elif number == 13:
        print("\n>>> SIM Services\n")
    elif number == 0:
        print("\nGoodbye! 👋")
        break
    else:
        print("\nInvalid choice! Please try again.\n")
