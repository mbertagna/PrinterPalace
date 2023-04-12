import streamlit as st
import mysql.connector
from itertools import chain

db = mysql.connector.connect(
    host = "",
    user = "",
    password = "",
    database = "PrinterPalace"
)

st.markdown("<h1 style='text-align: center;'>New Record</h1>", unsafe_allow_html=True)

# back = st.button("Back")

# submit = st.button("Submit")
    
# MYSQL

cursor = db.cursor()

def add_printer_model(printer_model):
    cursor.execute(
        ''' INSERT INTO printer_model VALUES(%s,%s,%s,%s,%s,%s);''', 
        printer_model
    )
    db.commit()

def add_fff_printer(fff_printer):
    cursor.execute(
        ''' INSERT INTO fff_printer(printer_name, model_name, current_nozzle_type, current_nozzle_size, current_bed_type, current_filament_id) 
              VALUES(%s,%s,%s,%s,%s,%s);''', 
        fff_printer
    )
    db.commit()

def add_sla_printer(sla_printer):
    cursor.execute(
        ''' INSERT INTO sla_printer(printer_name, model_name, current_resin_id) 
              VALUES(%s,%s,%s);''', 
        sla_printer
    )
    db.commit()

def add_filament(filament):
    cursor.execute(
        ''' INSERT INTO filament(filament_type, brand_name, color, quantity)
              VALUES(%s,%s,%s,%s);''', 
        filament
    )
    db.commit()

def add_resin(resin):
    cursor.execute(
        ''' INSERT INTO resin(brand_name, color, quantity)
              VALUES(%s,%s,%s);''', 
        resin
    )
    db.commit()

def update_filament(filament):
    cursor.execute(
        '''SELECT quantity
            FROM filament
            WHERE (filament_type = %s) AND (brand_name = %s) AND (color = %s);''',
    filament[0:3]
    )

    num_tup = cursor.fetchall()
    num = num_tup[0][0]

    cursor.execute(
    '''UPDATE filament SET quantity = %s + %s
        WHERE (filament_type = %s) AND (brand_name = %s) AND (color = %s);''',
    (filament[3], num, filament[0], filament[1], filament[2])
    )
    db.commit()

def update_resin(resin):
    cursor.execute(
        '''SELECT quantity
            FROM resin
            WHERE (brand_name = %s) AND (color = %s);''',
    (resin[0:2])
    )

    num_tup = cursor.fetchall()
    num = num_tup[0][0]

    cursor.execute(
    '''UPDATE resin SET quantity = %s + %s
        WHERE (brand_name = %s) AND (color = %s);''',
    (resin[2], num, resin[0], resin[1])
    )
    db.commit()

# STREAMLIT

category = st.selectbox(
"Select a category :",
("","Printer Model", "FFF Printer", "SLA Printer", "Resin", "Filament")
)
        
if (category == "Printer Model"):
    model_name = st.text_input("Model :")
    brand_name = st.text_input("Brand :")
    printer_type = st.selectbox(
        "Type :",
        ("", "FFF", "SLA")
    )
    bed_width = st.number_input("Bed width :")
    bed_length = st.number_input("Bed length :")
    bed_height = st.number_input("Bed height :")
    printer_model_button = st.button("Commit")
    if printer_model_button:
        printer_model = (model_name.upper(), brand_name.upper(), printer_type.upper(), str(bed_width).upper(), str(bed_length).upper(), str(bed_height).upper())
        add_printer_model(printer_model)

elif (category == "FFF Printer"):
    printer_name = st.text_input("Name :")
    cursor.execute(
        """
        SELECT model_name
        FROM printer_model
        WHERE printer_type = "FFF"
        """
    )
    models = cursor.fetchall()
    models = list(chain(*models))
    model_name = st.selectbox(
        "Model :",
        (models)
    )
    current_nozzle_type = st.text_input("Nozzle type :")
    current_nozzle_size = st.number_input("Nozzle size :")
    current_bed_type = st.text_input("Bed type :")
    cursor.execute(
        """
        SELECT DISTINCT filament_type
        FROM filament
        """
    )
    filament_types = cursor.fetchall()
    filament_types = list(chain(*filament_types))
    filament_type = st.selectbox(
        "Filament type :",
        (filament_types)
    )
    cursor.execute(
        """
        SELECT DISTINCT brand_name
        FROM filament
        WHERE filament_type = %s
        """,
        (filament_type,)
    )
    filament_brands = cursor.fetchall()
    filament_brands = list(chain(*filament_brands))
    filament_brand = st.selectbox(
        "Filament brand :",
        (filament_brands)
    )
    cursor.execute(
        """
        SELECT DISTINCT color
        FROM filament
        WHERE filament_type = %s AND brand_name = %s
        """,
        (filament_type, filament_brand)
    )
    colors = cursor.fetchall()
    colors = list(chain(*colors))
    filament_color = st.selectbox(
        "Filament color :",
        (colors)
    )
    cursor.execute(
        """
        SELECT filament_id
        FROM filament
        WHERE filament_type = %s AND brand_name = %s AND color = %s
        """,
        (filament_type, filament_brand, filament_color)
    )
    current_filament_id = cursor.fetchone()[0]
    fff_button = st.button("Commit")
    if fff_button:
        fff_printer = (printer_name.upper(), model_name.upper(), current_nozzle_type.upper(), str(current_nozzle_size).upper(), current_bed_type.upper(), str(current_filament_id).upper())
        add_fff_printer(fff_printer)

elif (category == "SLA Printer"):
    printer_name = st.text_input("Name :")
    cursor.execute(
        """
        SELECT model_name
        FROM printer_model
        WHERE printer_type = "SLA"
        """
    )
    models = cursor.fetchall()
    models = list(chain(*models))
    model_name = st.selectbox(
        "Model :",
        (models)
    )
    cursor.execute(
        """
        SELECT DISTINCT brand_name
        FROM resin
        """
    )
    resin_names = cursor.fetchall()
    resin_names = list(chain(*resin_names))
    resin_name = st.selectbox(
        "Resin brand name :",
        (resin_names)
    )
    cursor.execute(
        """
        SELECT DISTINCT color
        FROM resin
        WHERE brand_name = %s
        """,
        (resin_name,)
    )
    resin_colors = cursor.fetchall()
    resin_colors = list(chain(*resin_colors))
    resin_color = st.selectbox(
        "Resin color :",
        (resin_colors)
    )
    cursor.execute(
        """
        SELECT resin_id
        FROM resin
        WHERE brand_name = %s AND color = %s
        """,
        (resin_name.upper(), resin_color.upper())
    )
    current_resin_id = cursor.fetchone()[0]
    sla_button = st.button("Commit")
    if sla_button:
        sla_printer = (printer_name, model_name, current_resin_id)
        add_sla_printer(sla_printer)

elif (category == "Resin"):
    brand_name = st.text_input("Brand :")
    color = st.text_input("Color :")
    cursor.execute(
        """
        SELECT *
        FROM resin
        WHERE (brand_name = %s) AND (color = %s);""",
        (brand_name.upper(), color.upper())
    )
    if (len(cursor.fetchall()) == 0):
        resin_exists = False
    else:
        resin_exists = True
    quantity = st.number_input("Quantity :")
    resin_button = st.button("Commit")
    if resin_button:
        resin = (brand_name.upper(), color.upper(), str(quantity).upper())
        if not resin_exists:
            add_resin(resin)
        else:
            update_resin(resin)

elif (category == "Filament"):
    filament_type = st.text_input("Type :")
    brand_name = st.text_input("Brand :")
    color = st.text_input("Color :")
    cursor.execute(
        """
        SELECT *
        FROM filament
        WHERE (brand_name = %s) AND (color = %s) AND (filament_type = %s);""",
        (brand_name.upper(), color.upper(), filament_type.upper())
    )
    if (len(cursor.fetchall()) == 0):
        filament_exists = False
    else:
        filament_exists = True
    quantity = st.number_input("Quantity :")
    filament_button = st.button("Commit")
    if filament_button:
        filament = (filament_type.upper(), brand_name.upper(), color.upper(), str(quantity).upper())
        if not filament_exists:
            add_filament(filament)
        else:
            update_filament(filament)
