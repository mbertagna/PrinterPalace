import streamlit as st
import pandas as pd
import mysql.connector
from itertools import chain


db = mysql.connector.connect(
    host = "",
    user = "",
    password = "",
    database = "PrinterPalace"
)


st.markdown("<h1 style='text-align: center;'>Delete</h1>", unsafe_allow_html=True)

cursor = db.cursor()

category = st.selectbox(
"Select a category :",
("","Printer Model", "FFF Printer", "SLA Printer", "Resin", "Filament")
)


if (category == "Printer Model"):
    st.subheader("Filters :")
    model_name = "%" + st.text_input("Model :") + "%"
    brand_name = "%" + st.text_input("Brand :") + "%" 
    printer_type = "%" + st.text_input("Type :") + "%"
    printer_model_button = st.button("Search")
    
    if (printer_model_button):
        cursor.execute(
                    """
                    SELECT *
                    FROM printer_model
                    WHERE printer_model.model_name LIKE %s
                        AND brand_name LIKE %s
                        AND printer_type LIKE %s
                    """,
                    (model_name.upper(), brand_name.upper(), printer_type.upper())
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)
        delete = st.button("Delete Records")
        if (delete):
            cursor.execute(
                    """
                    DELETE FROM printer_model
                    WHERE printer_model.model_name LIKE %s
                        AND brand_name LIKE %s
                        AND printer_type LIKE %s
                    """,
                    (model_name.upper(), brand_name.upper(), printer_type.upper())
            )

elif (category == "FFF Printer"):
    st.subheader("Filters :")
    printer_name = "%" + st.text_input("Name :") + "%"
    model_name = "%" + st.text_input("Model :") + "%"
    current_nozzle_type = "%" + st.text_input("Nozzle type :") + "%"
    current_bed_type = "%" + st.text_input("Bed type :") + "%"

    fff_button = st.button("Search")
    
    if (fff_button):
        cursor.execute(
                    """
                    SELECT *
                    FROM fff_printer
                    WHERE printer_name LIKE %s
                        AND fff_printer.model_name LIKE %s
                        AND current_nozzle_type LIKE %s
                        AND current_bed_type LIKE %s
                    """,
                    (printer_name.upper(), model_name.upper(), current_nozzle_type.upper(), current_bed_type.upper())
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)
        delete = st.button("Delete")
        if (delete):
            cursor.execute(
                    """
                    DELETE FROM fff_printer
                    WHERE printer_name LIKE %s
                        AND fff_printer.model_name LIKE %s
                        AND current_nozzle_type LIKE %s
                        AND current_bed_type LIKE %s
                    """,
                    (printer_name.upper(), model_name.upper(), current_nozzle_type.upper(), current_bed_type.upper())
            )
elif (category == "SLA Printer"):
    st.subheader("Filters :")
    printer_name = "%" + st.text_input("Name :") + "%"
    model_name = "%" + st.text_input("Model :") + "%"

    sla_button = st.button("Search")
    
    if (sla_button):
        cursor.execute(
                    """
                    SELECT *
                    FROM sla_printer
                    WHERE printer_name LIKE %s
                        AND sla_printer.model_name LIKE %s
                    """,
                    (printer_name.upper(), model_name.upper())
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)
        delete = st.button("Delete")
        if (delete):
            cursor.execute(
                    """
                    DELETE FROM sla_printer
                    WHERE printer_name LIKE %s
                        AND sla_printer.model_name LIKE %s
                    """,
                    (printer_name.upper(), model_name.upper())
            )
elif (category == "Filament"):
    st.subheader("Filters :")
    filament_type = "%" + st.text_input("Type :") + "%"
    brand_name = "%" + st.text_input("Brand :") + "%"
    color = "%" + st.text_input("Color :") + "%"

    filament_button = st.button("Search")
    
    if (filament_button):
        cursor.execute(
                    """
                    SELECT *
                    FROM fff_printer
                    WHERE filament_type LIKE %s
                        AND brand_name LIKE %s
                        AND color LIKE %s
                    """,
                    (filament_type.upper(), brand_name.upper(), color.upper())
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)
        delete = st.button("Delete")
        if (delete):
            cursor.execute(
                    """
                    DELETEFROM fff_printer
                    WHERE filament_type LIKE %s
                        AND brand_name LIKE %s
                        AND color LIKE %s
                    """,
                    (filament_type.upper(), brand_name.upper(), color.upper())
            )
elif (category == "Resin"):
    st.subheader("Filters :")
    brand_name = "%" + st.text_input("Brand :") + "%"
    color = "%" + st.text_input("Color :") + "%"

    resin_button = st.button("Search")
    
    if (resin_button):
        cursor.execute(
                    """
                    SELECT * 
                    FROM sla_printer
                    WHERE brand_name LIKE %s
                        AND color LIKE %s
                    """,
                    (brand_name.upper(), color.upper())
            )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)
        delete = st.button("Delete")
        if (delete):
            cursor.execute(
                    """
                    DELETE FROM sla_printer
                    WHERE brand_name LIKE %s
                        AND color LIKE %s
                    """,
                    (brand_name.upper(), color.upper())
            )

