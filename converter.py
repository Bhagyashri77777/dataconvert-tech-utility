# A simple utility to convert data storage sizes for AI-DS
print("--- 💾 Welcome to Neural Knights DataConvert 💾 ---")

while True:
    print("\n--- Main Menu ---")
    print("1. Convert Megabytes (MB) to Gigabytes (GB)")
    print("2. Convert Gigabytes (GB) to Terabytes (TB)")
    print("3. Exit the tool")
    
    choice = input("What do you want to do? (Enter 1, 2, or 3): ")
    
    if choice == '1':
        mb = float(input("Enter data size in Megabytes (MB): "))
        gb = mb / 1024
        
        print("\n--- 📊 Conversion Result ---")
        print(mb, "MB is equal to", round(gb, 3), "GB")
        print("Status: Conversion successful! ✅")
        
    elif choice == '2':
        gb = float(input("Enter data size in Gigabytes (GB): "))
        tb = gb / 1024
        
        print("\n--- 📊 Conversion Result ---")
        print(gb, "GB is equal to", round(tb, 3), "TB")
        print("Status: Conversion successful! ✅")
        
    elif choice == '3':
        print("Bye! Exiting DataConvert...")
        print("Keep coding for Google! ✨ - Built by Bhagyashri Gawali")
        break
        
    else:
        print("Wrong choice! Please enter 1, 2, or 3.")

