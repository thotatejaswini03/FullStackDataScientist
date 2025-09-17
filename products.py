import os
from supabase import create_client, Client
from dotenv import load_dotenv

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
    print("\nProducts List:")
    for product in resp.data:
        print(f"{product['prod_id']}: {product['name']} - ${product['price']} (Stock: {product['stock']})")
    print()

def update_product():
    prod_id = int(input("Enter product ID to update: ").strip())
    name = input("Enter new name (leave blank to skip): ").strip()
    price = input("Enter new price (leave blank to skip): ").strip()
    stock = input("Enter new stock (leave blank to skip): ").strip()

    data = {}
    if name:
        data["name"] = name
    if price:
        data["price"] = float(price)
    if stock:
        data["stock"] = int(stock)

    if data:
        resp = sb.table("products").update(data).eq("prod_id", prod_id).execute()
        print("Product updated:", resp.data)
    else:
        print("No changes made.")

def delete_product():
    prod_id = int(input("Enter product ID to delete: ").strip())

    # Check if product is referenced in order_items
    ref_check = sb.table("order_items").select("*").eq("prod_id", prod_id).execute()
    if ref_check.data:
        print("Cannot delete this product because it's referenced in existing orders.")
        return

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
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
