# Core Pkgs
import streamlit as st 
import pandas as pd

# DB Mgmt
import sqlite3 
conn = sqlite3.connect('data/world.sqlite')
c = conn.cursor()


# Fxn Make Execution
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 


city = ['ID,', 'Name,', 'CountryCode,', 'District,', 'Population']
country = ['Code,', 'Name,', 'Continent,', 'Region,', 'SurfaceArea,', 'IndepYear,', 'Population,', 'LifeExpectancy,', 'GNP,', 'GNPOld,', 'LocalName,', 'GovernmentForm,', 'HeadOfState,', 'Capital,', 'Code2']
countrylanguage = ['CountryCode,', 'Language,', 'IsOfficial,', 'Percentage']




def main():
	st.title("Sqlify - Playground")

	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)


	if choice == "Home":
		st.subheader("Execute Queries Here")

		# Columns/Layout
		col1,col2 = st.columns(2)

		with col1:
			with st.form(key='query_form'):
				raw_code = st.text_area("SQL Code Here")
				submit_code = st.form_submit_button("Execute")
			with st.info('click'):
				st.markdown('Click below for overview of sample Data')
			# Table of Info
        
			with st.expander("Table Info"):
				table_info = {'city':city,'country':country,'countrylanguage':countrylanguage}
				st.json(table_info)
		# Results Layouts
		with col2:
			if submit_code:
				st.info("Query Submitted")
				st.code(raw_code)

				# Results 
				query_results = sql_executor(raw_code)
				with st.expander("Results"):
					st.write(query_results)

				with st.expander("Pretty Table"):
					query_df = pd.DataFrame(query_results)
					st.dataframe(query_df)


	else:
         st.markdown("""
                # About us

Welcome to the SQL Playground, a web-based tool for learning and practicing SQL (Structured Query Language). Whether you're a beginner looking to get started with SQL or an experienced database professional, this playground is a valuable resource for honing your SQL skills.

## Features

- **Interactive SQL Queries:** Write and execute SQL queries directly in your web browser. See immediate results to help you learn and troubleshoot.

- **Database Integration:** Connect to a sample database or use your own. Our playground supports various database systems, such as MySQL, PostgreSQL, SQLite, and more.

- **Query History:** Save and access your previous queries for future reference and study.

- **Syntax Highlighting:** Enjoy code highlighting and error detection to write clean and efficient SQL queries.

## How to Use

1. Select your preferred database system from the dropdown menu.
2. Write your SQL query in the provided code editor.
3. Click the "Run" button to execute your query.
4. View the results in the output panel.
5. Save your queries or download the results for later use.

## Example Queries

To help you get started, here are a few example queries you can try:

```sql
-- Retrieve all records from the "customers" table
SELECT * FROM city;

-- Find the total number of orders placed by each customer
SELECT name, COUNT(*) as city
FROM city
GROUP BY name;

        """)        




if __name__ == '__main__':
	main()