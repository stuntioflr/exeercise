import streamlit as st
import snowflake.connector

# Function to execute queries on Snowflake
def execute_query(query, config):
    try:
        con = snowflake.connector.connect(
            user=config['username'],
            password=config['password'],
            account=config['account_url'],
            warehouse=config['warehouse'],
            database=config['database'],
            schema=config['schema']
        )
        cursor = con.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        st.table(result)
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
    config_visible = st.button("Configure Snowflake")
    config = {}
    if config_visible:
        config['username'] = st.text_input("Username")
        config['password'] = st.text_input("Password", type="password")
        config['account_url'] = st.text_input("Account URL")
        config['warehouse'] = st.text_input("Warehouse")
        config['database'] = st.text_input("Database")
        config['schema'] = st.text_input("Schema")
        submit_button = st.button("Connect")

        # Execute queries if form submitted
        if submit_button:
            query = st.text_area("Enter your query")
            execute_query(query, config)

if __name__ == '__main__':
    main()
