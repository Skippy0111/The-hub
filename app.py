import streamlit as st
import pandas as pd

# Sample data for property listings
property_data = pd.DataFrame({
    'Property': ['Property A', 'Property B', 'Property C'],
    'Description': ['3 Bed, 2 Bath', '4 Bed, 3 Bath', '2 Bed, 1 Bath'],
    'Price': ['$250,000', '$350,000', '$200,000'],
    'Contact': ['John Doe', 'Jane Smith', 'Bob Johnson'],
    'Images': ['property_a.jpg', 'property_b.jpg', 'property_c.jpg']
})

# Sample data for cash buyers and fix and flip buyers
cash_buyers_data = pd.DataFrame({
    'Name': ['Cash Buyer 1', 'Cash Buyer 2'],
    'Criteria': ['Criteria A', 'Criteria B'],
    'Contact': ['Email: cashbuyer1@example.com', 'Phone: 123-456-7890']
})

flip_buyers_data = pd.DataFrame({
    'Name': ['Flip Buyer 1', 'Flip Buyer 2'],
    'Criteria': ['Criteria X', 'Criteria Y'],
    'Contact': ['Email: flipbuyer1@example.com', 'Phone: 987-654-3210']
})

def main():
    st.title("Real Estate Wholesalers Hub")

    # Navigation
    section = st.sidebar.radio("Select Section", ["List Property", "Cash Buyers", "Fix and Flip Buyers", "Showcase Deals"])

    if section == "List Property":
        list_property()
    elif section == "Cash Buyers":
        show_cash_buyers()
    elif section == "Fix and Flip Buyers":
        show_flip_buyers()
    elif section == "Showcase Deals":
        showcase_deals()

def list_property():
    st.header("List Your Property")

    # Add form for property listing (e.g., property details, price, contact information)
    property_name = st.text_input("Property Name")
    description = st.text_input("Description")
    price = st.text_input("Price")
    contact = st.text_input("Contact Person")

    # Upload image
    uploaded_image = st.file_uploader("Upload Property Image", type=["jpg", "jpeg", "png"])

    if st.button("List Property"):
        # Store the property information (you may want to save it to a database)
        property_data.loc[len(property_data)] = [property_name, description, price, contact, '']

        st.success(f"Property '{property_name}' listed successfully!")

def show_cash_buyers():
    st.header("Cash Buyers")

    # Display a table of cash buyers with their criteria and contact information
    st.table(cash_buyers_data)

def show_flip_buyers():
    st.header("Fix and Flip Buyers")

    # Display a table of fix and flip buyers with their criteria and contact information
    st.table(flip_buyers_data)

def showcase_deals():
    st.header("Showcase Deals")

    # Display images of showcased deals
    for index, row in property_data.iterrows():
        st.subheader(row['Property'])
        st.write(f"Description: {row['Description']}")
        st.write(f"Price: {row['Price']}")
        st.write(f"Contact: {row['Contact']}")
        image = row['Images']
        if image:
            st.image(image, caption=row['Property'], use_column_width=True)
        else:
            st.write("No image available for this property.")

if __name__ == "__main__":
    main()


    
       
      
      
 

  

    
   
  
  
