from supabase import create_client, Client
from config import SUPABASE_SERVICE_ROLE_KEY, SUPABASE_URL

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

def save_to_supabase(product_as_json):
    message = ""
    try:
        response = (
            supabase.table("products")
            .insert(product_as_json)
            .execute()
        )
        message = "successful"
        print("Successfully saved:", response)
    except Exception as e:
        print(e)
        message = "shit"
    finally:
        return message
