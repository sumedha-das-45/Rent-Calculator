# Rent Calculator App

def calculate_rent():
    try:
        total_rent = float(input("Enter total monthly rent (₹): "))
        num_roommates = int(input("Enter number of roommates: "))

        include_utilities = input("Include utilities? (yes/no): ").strip().lower()
        utilities = 0
        if include_utilities == 'yes':
            utilities = float(input("Enter total utilities cost (₹): "))

        total_amount = total_rent + utilities
        rent_per_person = total_amount / num_roommates

        print("\n===== Rent Summary =====")
        print(f"Total Rent: ₹{total_rent:.2f}")
        print(f"Utilities: ₹{utilities:.2f}")
        print(f"Total Monthly Amount: ₹{total_amount:.2f}")
        print(f"Each person pays: ₹{rent_per_person:.2f}")
        print("=========================")
    
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")

def main():
    print("🏠 Welcome to the Rent Calculator App 🏠")
    while True:
        calculate_rent()
        again = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("👋 Goodbye! Hope your rent splitting goes well.")
            break

if __name__ == "__main__":
    main()
