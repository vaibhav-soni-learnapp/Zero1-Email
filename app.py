import streamlit as st
import requests
import pandas as pd

# URL from which data will be fetched
URL = "https://crates.zero1byzerodha.com/users/fetch/emails"

#URL = "https://crates.zero1byzerodha.com/users/fetch/emails"
def fetch_data(url):
    """Fetch data from the specified URL and return a DataFrame."""
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['items'])
        return df
    else:
        st.error(f"Failed to fetch data: HTTP Status Code {response.status_code}")
        return pd.DataFrame()

def main():
    """Main function to run the Streamlit app."""
    st.title("✌️Varsity Live Mission (Zero1 Fest)")

    # Button to trigger data loading
    if st.button("Fetch Emails"):
        df = fetch_data(URL)
        if not df.empty:
            st.write("Emails fetched successfully!")
            st.dataframe(df)
        else:
            st.write("No data to display.")

if __name__ == "__main__":
    main()
