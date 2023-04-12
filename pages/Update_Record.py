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

st.markdown("<h1 style='text-align: center;'>Update</h1>", unsafe_allow_html=True)

# STREAMLIT

# update all fields everytime there is any update by using old values for simplification

cursor = db.cursor()

category = st.selectbox(
"Select record type :",
("","Printer Model", "FFF Printer", "Nozzle Swap", "SLA Printer", "Resin", "Filament")
)

if category == "Printer Model":
    model_name = st.text_input("Model :")
    brand_name = st.text_input("Brand :")
    printer_type = st.selectbox(
        "Type :",
        ("", "FFF", "SLA")
    )
    bed_width = st.number_input("Bed width :")
    bed_length = st.number_input("Bed length :")
    bed_height = st.number_input("Bed height :")

    mod_value = st.selectbox(
        "Value to modify:",
        ("", "Model", "Brand", "Type", "Bed width", "Bed length", "Bed height")
    )

    if bed_height == 0:
        bh_low = "0"
        bh_high = "9999999"
    else:
        bh_low = str(bed_height)
        bh_high = str(bed_height)


    if bed_width == 0:
        bw_low = "0"
        bw_high = "9999999"
    else:
        bw_low = str(bed_width)
        bw_high = str(bed_width)

    if bed_length == 0:
        bl_low = "0"
        bl_high = "9999999"
    else:
        bl_low = str(bed_length)
        bl_high = str(bed_length)

    values_to_update = ("%"+model_name.upper()+"%", "%"+brand_name.upper()+"%", "%"+printer_type.upper()+"%", bw_low, bw_high, bl_low, bl_high, bh_low, bh_high)

    if mod_value == "Model":
        mod = "model_name"
        
        cursor.execute(
            """
            SELECT * FROM printer_model
            WHERE printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.text_input("New Model :")
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE printer_model SET '''+mod+''' = %s
            WHERE
            printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;''', (new_value.upper(),) + values_to_update)

    if mod_value == "Brand":
        mod = "brand_name"

        cursor.execute(
            """
            SELECT * FROM printer_model
            WHERE printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.text_input("New Brand :")
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE printer_model SET '''+mod+''' = %s
            WHERE
            printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;''', (new_value.upper(),) + values_to_update)

    if mod_value == "Type":
        mod = "printer_type"

        cursor.execute(
            """
            SELECT * FROM printer_model
            WHERE printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.selectbox(
            "New Type :",
            ("", "FFF", "SLA")
        )
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE printer_model SET '''+mod+''' = %s
            WHERE
            printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;''', (new_value.upper(),) + values_to_update)

    if mod_value == "Bed width":
        mod = "bed_width"

        cursor.execute(
            """
            SELECT * FROM printer_model
            WHERE printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = str(st.number_input("New Bed width :"))

        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE printer_model SET '''+mod+''' = %s
            WHERE
            printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;''', (new_value.upper(),) + values_to_update)

    if mod_value == "Bed length":
        mod = "bed_length"

        cursor.execute(
            """
            SELECT * FROM printer_model
            WHERE printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = str(st.number_input("New Bed length :"))
                
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE printer_model SET '''+mod+''' = %s
            WHERE
            printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;''', (new_value.upper(),) + values_to_update)       

    if mod_value == "Bed height":
        mod = "bed_height"

        cursor.execute(
            """
            SELECT * FROM printer_model
            WHERE printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = str(st.number_input("New Bed height :"))
                
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE printer_model SET '''+mod+''' = %s
            WHERE
            printer_model.model_name LIKE %s
            AND brand_name LIKE %s
            AND printer_type LIKE %s
            AND bed_width BETWEEN %s AND %s
            AND bed_length BETWEEN %s AND %s
            AND bed_height BETWEEN %s AND %s;''', (new_value.upper(),) + values_to_update)


if category == "FFF Printer":

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
        [""]+(models)
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
        [""]+(filament_types)
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
        [""]+(filament_brands)
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
        [""]+(colors)
    )
    cursor.execute(
        """
        SELECT filament_id
        FROM filament
        WHERE filament_type = %s AND brand_name = %s AND color = %s
        """,
        (filament_type, filament_brand, filament_color)
    )
    current_filament_id = cursor.fetchall()
    current_filament_id = list(chain(*current_filament_id))

    if current_nozzle_size == 0:
        cns_low = "0"
        cns_high = "9999999"
    else:
        cns_low = str(current_nozzle_size)
        cns_high = str(current_nozzle_size)

    if current_filament_id == []:
        cfid_low = "0"
        cfid_high = "9999999"
    else:
        cfid_low = str(current_filament_id[0])
        cfid_high = str(current_filament_id[0])

    values_to_update = ("%"+printer_name.upper()+"%", "%"+model_name.upper()+"%", "%"+current_nozzle_type.upper()+"%", cns_low, cns_high, "%"+current_bed_type.upper()+"%", cfid_low, cfid_high)

    mod_value = st.selectbox(
        "Value to modify:",
        ("", "Name", "Model", "Nozzle type", "Nozzle size", "Bed type", "Current filament")
    )

    if mod_value == "Name":
        mod = "printer_name"
        
        cursor.execute(
            """
            SELECT printer_name, model_name, current_nozzle_type, current_nozzle_size, current_bed_type, filament_type, brand_name, color
            FROM fff_printer
            INNER JOIN filament f on fff_printer.current_filament_id = f.filament_id
            WHERE
            printer_name LIKE %s
            AND model_name LIKE %s
            AND current_nozzle_type LIKE %s
            AND current_nozzle_size BETWEEN %s and %s
            AND current_bed_type LIKE %s
            AND current_filament_id BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.text_input("New Name :")
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE fff_printer
            SET '''+mod+''' = %s
            WHERE
            printer_name LIKE %s
            AND model_name LIKE %s
            AND current_nozzle_type LIKE %s
            AND current_nozzle_size BETWEEN %s and %s
            AND current_bed_type LIKE %s
            AND current_filament_id BETWEEN %s AND %s;''', (new_value.upper(),) + values_to_update)


    if mod_value == "Model":
        mod = "model_name"

        cursor.execute(
            """
            SELECT printer_name, model_name, current_nozzle_type, current_nozzle_size, current_bed_type, filament_type, brand_name, color
            FROM fff_printer
            INNER JOIN filament f on fff_printer.current_filament_id = f.filament_id
            WHERE
            printer_name LIKE %s
            AND model_name LIKE %s
            AND current_nozzle_type LIKE %s
            AND current_nozzle_size BETWEEN %s and %s
            AND current_bed_type LIKE %s
            AND current_filament_id BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.text_input("New Model :")
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE fff_printer
            SET '''+mod+''' = %s
            WHERE
            printer_name LIKE %s
            AND model_name LIKE %s
            AND current_nozzle_type LIKE %s
            AND current_nozzle_size BETWEEN %s and %s
            AND current_bed_type LIKE %s
            AND current_filament_id BETWEEN %s AND %s;''', (new_value.upper(),) + values_to_update)


    if mod_value == "Nozzle type":
        mod = "current_nozzle_type"

        cursor.execute(
            """
            SELECT printer_name, model_name, current_nozzle_type, current_nozzle_size, current_bed_type, filament_type, brand_name, color
            FROM fff_printer
            INNER JOIN filament f on fff_printer.current_filament_id = f.filament_id
            WHERE
            printer_name LIKE %s
            AND model_name LIKE %s
            AND current_nozzle_type LIKE %s
            AND current_nozzle_size BETWEEN %s and %s
            AND current_bed_type LIKE %s
            AND current_filament_id BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.text_input("New Nozzle type :")
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE fff_printer
            SET '''+mod+''' = %s
            WHERE
            printer_name LIKE %s
            AND model_name LIKE %s
            AND current_nozzle_type LIKE %s
            AND current_nozzle_size BETWEEN %s and %s
            AND current_bed_type LIKE %s
            AND current_filament_id BETWEEN %s AND %s;''', (new_value.upper(),) + values_to_update)

    if mod_value == "Nozzle size":
        mod = "current_nozzle_size"

        cursor.execute(
            """
            SELECT printer_name, model_name, current_nozzle_type, current_nozzle_size, current_bed_type, filament_type, brand_name, color
            FROM fff_printer
            INNER JOIN filament f on fff_printer.current_filament_id = f.filament_id
            WHERE
            printer_name LIKE %s
            AND model_name LIKE %s
            AND current_nozzle_type LIKE %s
            AND current_nozzle_size BETWEEN %s and %s
            AND current_bed_type LIKE %s
            AND current_filament_id BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.number_input("New Nozzle size :")
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE fff_printer
            SET '''+mod+''' = %s
            WHERE
            printer_name LIKE %s
            AND model_name LIKE %s
            AND current_nozzle_type LIKE %s
            AND current_nozzle_size BETWEEN %s and %s
            AND current_bed_type LIKE %s
            AND current_filament_id BETWEEN %s AND %s;''', (str(new_value).upper(),) + values_to_update)


    if mod_value == "Bed type":
        mod = "current_bed_type"

        cursor.execute(
            """
            SELECT printer_name, model_name, current_nozzle_type, current_nozzle_size, current_bed_type, filament_type, brand_name, color
            FROM fff_printer
            INNER JOIN filament f on fff_printer.current_filament_id = f.filament_id
            WHERE
            printer_name LIKE %s
            AND model_name LIKE %s
            AND current_nozzle_type LIKE %s
            AND current_nozzle_size BETWEEN %s and %s
            AND current_bed_type LIKE %s
            AND current_filament_id BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.text_input("New Bed type :")
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE fff_printer
            SET '''+mod+''' = %s
            WHERE
            printer_name LIKE %s
            AND model_name LIKE %s
            AND current_nozzle_type LIKE %s
            AND current_nozzle_size BETWEEN %s and %s
            AND current_bed_type LIKE %s
            AND current_filament_id BETWEEN %s AND %s;''', (new_value.upper(),) + values_to_update)


    if mod_value == "Current filament":
        mod = "current_filament_id"

        cursor.execute(
            """
            SELECT printer_name, model_name, current_nozzle_type, current_nozzle_size, current_bed_type, filament_type, brand_name, color
            FROM fff_printer
            INNER JOIN filament f on fff_printer.current_filament_id = f.filament_id
            WHERE
            printer_name LIKE %s
            AND model_name LIKE %s
            AND current_nozzle_type LIKE %s
            AND current_nozzle_size BETWEEN %s and %s
            AND current_bed_type LIKE %s
            AND current_filament_id BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)


        cursor.execute(
            """
            SELECT DISTINCT filament_type
            FROM filament
            """
        )
        fil_types = cursor.fetchall()
        fil_types = list(chain(*fil_types))
        fil_type = st.selectbox(
            "New Filament type :",
            [""]+(fil_types)
        )
        cursor.execute(
            """
            SELECT DISTINCT brand_name
            FROM filament
            WHERE filament_type = %s
            """,
            (fil_type,)
        )
        fil_brands = cursor.fetchall()
        fil_brands = list(chain(*fil_brands))
        fil_brand = st.selectbox(
            "New Filament brand :",
            [""]+(fil_brands)
        )
        cursor.execute(
            """
            SELECT DISTINCT color
            FROM filament
            WHERE filament_type = %s AND brand_name = %s
            """,
            (fil_type, fil_brand)
        )
        col = cursor.fetchall()
        col = list(chain(*col))
        fil_color = st.selectbox(
            "New Filament color :",
            [""]+(col)
        )
        cursor.execute(
            """
            SELECT filament_id
            FROM filament
            WHERE filament_type = %s AND brand_name = %s AND color = %s
            """,
            (fil_type, fil_brand, fil_color)
        )
        new_value = cursor.fetchall()
        new_value = list(chain(*new_value))

        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE fff_printer
            SET '''+mod+''' = %s
            WHERE
            printer_name LIKE %s
            AND model_name LIKE %s
            AND current_nozzle_type LIKE %s
            AND current_nozzle_size BETWEEN %s and %s
            AND current_bed_type LIKE %s
            AND current_filament_id BETWEEN %s AND %s;''', (str(new_value[0]).upper(),) + values_to_update)


if category == "SLA Printer":

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
        [""]+(models)
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
        [""]+(resin_names)
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
        [""]+(resin_colors)
    )
    cursor.execute(
        """
        SELECT resin_id
        FROM resin
        WHERE brand_name = %s AND color = %s
        """,
        (resin_name.upper(), resin_color.upper())
    )
    current_resin_id = cursor.fetchall()
    current_resin_id = list(chain(*current_resin_id))



    if current_resin_id == []:
        crid_low = "0"
        crid_high = "9999999"
    else:
        crid_low = str(current_resin_id[0])
        crid_high = str(current_resin_id[0])

    values_to_update = ("%"+printer_name.upper()+"%", "%"+model_name.upper()+"%", crid_low, crid_high)

    mod_value = st.selectbox(
        "Value to modify:",
        ("", "Name", "Model", "Current resin")
    )

    if mod_value == "Name":
        mod = "printer_name"
        
        cursor.execute(
            """
            SELECT printer_name, model_name, brand_name, color
            FROM sla_printer
            INNER JOIN resin r on sla_printer.current_resin_id = r.resin_id
            WHERE
            printer_name LIKE %s
            AND model_name LIKE %s
            AND current_resin_id BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.text_input("New Name :")
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE sla_printer
        SET '''+mod+''' = %s
        WHERE
        printer_name LIKE %s
        AND model_name LIKE %s
        AND current_resin_id BETWEEN %s AND %s;''', (new_value.upper(),) + values_to_update)


    if mod_value == "Model":
        mod = "model_name"

        cursor.execute(
            """
        SELECT printer_name, model_name, brand_name, color
        FROM sla_printer
        INNER JOIN resin r on sla_printer.current_resin_id = r.resin_id
        WHERE
        printer_name LIKE %s
        AND model_name LIKE %s
        AND current_resin_id BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.text_input("New Model :")
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE sla_printer
        SET '''+mod+''' = %s
        WHERE
        printer_name LIKE %s
        AND model_name LIKE %s
        AND current_resin_id BETWEEN %s AND %s;''', (new_value.upper(),) + values_to_update)




    if mod_value == "Current resin":
        mod = "current_resin_id"

        cursor.execute(
            """
            SELECT printer_name, model_name, brand_name, color
            FROM sla_printer
            INNER JOIN resin r on sla_printer.current_resin_id = r.resin_id
            WHERE
            printer_name LIKE %s
            AND model_name LIKE %s
            AND current_resin_id BETWEEN %s AND %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)


        cursor.execute(
            """
            SELECT DISTINCT brand_name
            FROM resin
            """
        )
        res_names = cursor.fetchall()
        res_names = list(chain(*res_names))
        res_name = st.selectbox(
            "New Resin brand name :",
            [""]+(res_names)
        )
        cursor.execute(
            """
            SELECT DISTINCT color
            FROM resin
            WHERE brand_name = %s
            """,
            (res_name,)
        )
        res_colors = cursor.fetchall()
        res_colors = list(chain(*res_colors))
        res_color = st.selectbox(
            "New Resin color :",
            [""]+(res_colors)
        )
        cursor.execute(
            """
            SELECT resin_id
            FROM resin
            WHERE brand_name = %s AND color = %s
            """,
            (res_name.upper(), res_color.upper())
        )
        new_value = cursor.fetchall()
        new_value = list(chain(*new_value))

        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE sla_printer
        SET '''+mod+''' = %s
        WHERE
        printer_name LIKE %s
        AND model_name LIKE %s
        AND current_resin_id BETWEEN %s AND %s;''', (str(new_value[0]).upper(),) + values_to_update)


if category == "Resin":
    brand_name = st.text_input("Brand :")
    color = st.text_input("Color :")

    values_to_update = ("%"+brand_name.upper()+"%", "%"+color.upper()+"%")

    mod_value = st.selectbox(
        "Value to modify:",
        ("", "Brand", "Color")
    )

    if mod_value == "Brand":
        mod = "brand_name"
        
        cursor.execute(
            """
            SELECT brand_name, color
            FROM resin
            WHERE
            brand_name LIKE %s
            AND color LIKE %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.text_input("New Brand :")
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE resin
        SET '''+mod+''' = %s
        WHERE
        brand_name LIKE %s
        AND color LIKE %s;''', (new_value.upper(),) + values_to_update)

    if mod_value == "Color":
        mod = "color"

        cursor.execute(
            """
            SELECT brand_name, color
            FROM resin
            WHERE
            brand_name LIKE %s
            AND color LIKE %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.text_input("New Color :")
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE resin
        SET '''+mod+''' = %s
        WHERE
        brand_name LIKE %s
        AND color LIKE %s;''', (new_value.upper(),) + values_to_update)


if category == "Filament":
    filament_type = st.text_input("Type :")
    brand_name = st.text_input("Brand :")
    color = st.text_input("Color :")

    values_to_update = ("%"+filament_type+"%", "%"+brand_name.upper()+"%", "%"+color.upper()+"%")

    mod_value = st.selectbox(
        "Value to modify:",
        ("", "Type", "Brand", "Color")
    )

    if mod_value == "Type":
        mod = "filament_type"
        
        cursor.execute(
            """
        SELECT filament_type, brand_name, color
        FROM filament
        WHERE
        filament_type LIKE %s
        AND brand_name LIKE %s
        AND color LIKE %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.text_input("New Type :")
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE filament
        SET '''+mod+''' = %s
        WHERE
        filament_type LIKE %s
        AND brand_name LIKE %s
        AND color LIKE %s;''', (new_value.upper(),) + values_to_update)

    if mod_value == "Brand":
        mod = "brand_name"
        
        cursor.execute(
            """
        SELECT filament_type, brand_name, color
        FROM filament
        WHERE
        filament_type LIKE %s
        AND brand_name LIKE %s
        AND color LIKE %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.text_input("New Brand :")
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE filament
        SET '''+mod+''' = %s
        WHERE
        filament_type LIKE %s
        AND brand_name LIKE %s
        AND color LIKE %s;''', (new_value.upper(),) + values_to_update)

    if mod_value == "Color":
        mod = "color"

        cursor.execute(
            """
        SELECT filament_type, brand_name, color
        FROM filament
        WHERE
        filament_type LIKE %s
        AND brand_name LIKE %s
        AND color LIKE %s;
            """, values_to_update
        )
        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        st.write(df)

        new_value = st.text_input("New Color :")
        
        cmt = st.button("Commit")

        if cmt:
            cursor.execute(
        '''UPDATE filament
        SET '''+mod+''' = %s
        WHERE
        filament_type LIKE %s
        AND brand_name LIKE %s
        AND color LIKE %s;''', (new_value.upper(),) + values_to_update)















if (category == "Nozzle Swap"):
    cursor.execute(
        """
        SELECT printer_name FROM fff_printer
        ORDER BY printer_name;
        """
    )
    printers = cursor.fetchall()
    printers = list(chain(*printers))
    cursor.execute(
        """
        SELECT current_nozzle_type FROM fff_printer
        ORDER BY printer_name;
        """
    )
    nozzles = cursor.fetchall()
    nozzles = list(chain(*nozzles))

    printers = [""] + printers
    printer_1 = st.selectbox(
        "Printer 1 :",
        (printers))
    if printer_1 != "":
        p1idx = printers.index(printer_1)
        # st.text(nozzles[p1idx])

        printers_mod = printers
        nozzles_mod = nozzles

        # del printers_mod[p1idx]
        # del nozzles_mod[p1idx]

        printer_2 = st.selectbox(
        "Printer 2 :",
        (printers_mod))

        if printer_2 == printer_1:
            st.error("ERROR - Select 2 different printers")
        elif printer_2 != "":
            # with st.container():
            #     st.text(nozzles_mod[p1idx])
            button = st.button("Swap")
            if button:
                cursor.execute(
                    '''
                    START TRANSACTION;
                    CALL sp_getNozzle(%s, @t);
                    CALL sp_getNozzle(%s, @u);
                    SAVEPOINT x;
                    UPDATE fff_printer
                        SET current_nozzle_type = @t
                        WHERE printer_name = %s;
                    UPDATE fff_printer
                        SET current_nozzle_type = @u
                        WHERE printer_name = %s;
                    COMMIT;
                    '''
                    ,(printer_1, printer_2, printer_2, printer_1)
                )