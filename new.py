import streamlit as st
import snowflake.connector

# Function to execute queries on Snowflake
def execute_query(query):
    try:
        con = snowflake.connector.connect(
            user='<snowflake_username>',
            password='<snowflake_password>',
            account='<snowflake_account_url>',
            warehouse='<snowflake_warehouse>',
            database='<snowflake_database>',
            schema='<snowflake_schema>'
        )
        cursor = con.cursor()
        cursor.execute(query)
        st.success("Query executed successfully!")
    except Exception as e:
        st.error(f"Error executing query: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

# Streamlit UI
def main():
    st.title("Snowflake Query Execution")

    # Button to configure Snowflake connection
    if st.button("ep_config"):
        with st.form("connection_form"):
            st.subheader("Snowflake Configuration")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            account = st.text_input("Account URL")
            warehouse = st.text_input("Warehouse")
            database = st.text_input("Database")
            schema = st.text_input("Schema")
            submit_button = st.form_submit_button(label="Connect")

        # Execute queries if form submitted
        if submit_button:
            query = st.text_area("Enter your query")
            execute_query(query)

if __name__ == '__main__':
    main()
