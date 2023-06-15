import streamlit as st
import snowflake.connector

# Function to insert a record into Snowflake
def insert_record(config, data):
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
        query = f"INSERT INTO your_table_name (column1, column2, column3) VALUES ('{data['value1']}', '{data['value2']}', '{data['value3']}')"
        cursor.execute(query)
        con.commit()
        st.success("Record inserted successfully!")
    except Exception as e:
        st.error(f"Error inserting record: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

# Streamlit UI
def main():
    st.title("Insert Record into Snowflake Database")

    # Snowflake configuration
    config = {}
    config['username'] = st.text_input("Username")
    config['password'] = st.text_input("Password", type="password")
    config['account_url'] = st.text_input("Account URL")
    config['warehouse'] = st.text_input("Warehouse")
    config['database'] = st.text_input("Database")
    config['schema'] = st.text_input("Schema")

    # Record details
    st.subheader("Record Details")
    data = {}
    data['value1'] = st.text_input("Value 1")
    data['value2'] = st.text_input("Value 2")
    data['value3'] = st.text_input("Value 3")

    # Insert button
    if st.button("Insert Record"):
        insert_record(config, data)

if __name__ == '__main__':
    main()
