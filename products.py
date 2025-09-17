import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

sb: Client = create_client(url, key)

def create_product():
    name = input("Enter product name: ").strip()
    price = float(input("Enter price: ").strip())
    stock = int(input("Enter stock: ").strip())
    data = {"name": name, "price": price, "stock": stock}
    resp = sb.table("products").insert(data).execute()
    print("Product added:", resp.data)

def list_products():
    resp = sb.table("products").select("*").execute()
    products = resp.data
    print("\nProducts List:")
    for p in products:
        print(f"{p['prod_id']}: {p['name']} - ${p['price']} (Stock: {p['stock']})")

def update_product():
    prod_id = int(input("Enter product ID to update: ").strip())
    name = input("Enter new name (leave blank to skip): ").strip()
    price_input = input("Enter new price (leave blank to skip): ").strip()
    stock_input = input("Enter new stock (leave blank to skip): ").strip()

    updates = {}
    if name:
        updates["name"] = name
    if price_input:
        updates["price"] = float(price_input)
    if stock_input:
        updates["stock"] = int(stock_input)

    if updates:
        resp = sb.table("products").update(updates).eq("prod_id", prod_id).execute()
        print("Product updated:", resp.data)
    else:
        print("No updates provided.")

def delete_product():
    prod_id = int(input("Enter product ID to delete: ").strip())
    # Optional: Check if product exists before deleting
    resp = sb.table("products").delete().eq("prod_id", prod_id).execute()
    print("Product deleted:", resp.data)

def menu():
    while True:
        print("\nProduct CRUD Operations")
        print("1. Add Product")
        print("2. List Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            create_product()
        elif choice == "2":
            list_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
