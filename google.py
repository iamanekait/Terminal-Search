import webbrowser
from urllib.parse import quote

def google_search(query):
    try:
        # Format the query for the Google search URL
        query_encoded = quote(query)
        search_url = f"https://www.google.com/search?q={query_encoded}"

        # Open the browser and perform the search
        webbrowser.open_new_tab(search_url)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    search_query = input("Enter your search query: ")
    google_search(search_query)
