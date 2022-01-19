# For formatting pandas dataframes into excel reports


import pandas as pd
import numpy as np


def format_excel(filename, df, sheetname, rounded=2, total_row=False):
    """
    Function to auto fit the column widths and apply a table format style,
    when exporting excel sheets
    filename = str output filename
    sheetname = str Name to put on the excel sheet tab
    df = the pandas datframe to export to excel
    total_row = bool include a total column sum row
    """
    # truncate sheetname - -excel will not accept >31
    sheetname = sheetname[:30]

    # round to X sig figs
    df = df.round(rounded)

    # load excelwriter class and set date formats
    with pd.ExcelWriter(
        filename,
        engine="xlsxwriter",
        date_format="DD/MM/YYYY",
        datetime_format="DD/MM/YYYY",
    ) as writer:
        # send df to writer
        df.to_excel(writer, sheet_name=sheetname, index=False)
        # pull worksheet object
        worksheet = writer.sheets[sheetname]
        # loop through all columns
        for idx, col in enumerate(df):
            series = df[col]
            # len of largest item
            max_len = (
                max(
                    (
                        series.astype(str).map(len).max(),
                        len(str(series.name)),  # len of column name/header
                    )
                )
                + 2
            )  # adding a little extra space
            # set column width
            worksheet.set_column(idx, idx, max_len)

        # apply basic table format
        rows = len(df)
        cols = len(df.columns) - 1
        col_titles = []
        for c in df.columns:
            x = {"header": c}
            col_titles.append(x)
        worksheet.add_table(
            0,
            0,
            rows,
            cols,
            {
                "total_row": False,
                "columns": col_titles,
                "style": "Table Style Medium 2",
            },
        )



def format_excel_white(filename, df, sheetname, rounded=2):
    """
    Function to auto fit the column widths and apply a table format style,
    when exporting excel sheets
    filename = output filename
    sheetname = Name to put on the excel sheet tab
    df = datframe to export to excel
    """
    # truncate sheetname - -excel will not accept >31
    sheetname = sheetname[:30]

    # round to X sig figs
    df = df.round(rounded)

    # load excelwriter class and set date formats
    with pd.ExcelWriter(
        filename,
        engine="xlsxwriter",
        date_format="DD/MM/YYYY",
        datetime_format="DD/MM/YYYY",
    ) as writer:
        # send df to writer
        df.to_excel(writer, sheet_name=sheetname, index=False)
        # pull worksheet object
        worksheet = writer.sheets[sheetname]
        # loop through all columns
        for idx, col in enumerate(df):
            series = df[col]
            # len of largest item
            max_len = (
                max(
                    (
                        series.astype(str).map(len).max(),
                        len(str(series.name)),  # len of column name/header
                    )
                )
                + 2
            )  # adding a little extra space
            # set column width
            worksheet.set_column(idx, idx, max_len)

        # apply basic table format
        rows = len(df)
        cols = len(df.columns) - 1
        col_titles = []
        for c in df.columns:
            x = {"header": c}
            col_titles.append(x)
        worksheet.add_table(
            0,
            0,
            rows,
            cols,
            {
                "total_row": False,
                "columns": col_titles,
                "autofilter": False,
                "banded_rows": True,
                "banded_columns": False,
                "style": "Table Style Light 1",
            },
        )



def format_excel_currency(filename, df, sheetname, range1, range2):
    """
    Function to auto fit the column widths and apply a table format style,
    when exporting excel sheets
    filename = output filename
    sheetname = Name to put on the excel sheet tab
    df = datframe to export to excel
    range of excel columns to format
    """
    # truncate sheetname - -excel will not accept >31
    sheetname = sheetname[:30]
    # load excelwriter class and set date formats
    with pd.ExcelWriter(
        filename,
        engine="xlsxwriter",
        date_format="DD/MM/YYYY",
        datetime_format="DD/MM/YYYY",
    ) as writer:

        # send df to writer
        df.to_excel(writer, sheet_name=sheetname, index=False)
        # get the workbook object
        workbook = writer.book
        # pull worksheet object
        worksheet = writer.sheets[sheetname]
        # set the formats
        currency = workbook.add_format({"num_format": "£#,##0"})
        percent = workbook.add_format({"num_format": "0%"})
        # percentage = workbook.add_format({'num_format':'0.00%'})
        if range1:
            worksheet.set_column(range1, None, currency)
        if range2:
            worksheet.set_column(range2, None, percent)

        # loop through all columns
        for idx, col in enumerate(df):
            series = df[col]
            # len of largest item
            max_len = (
                max(
                    (
                        series.astype(str).map(len).max(),
                        len(str(series.name)),  # len of column name/header
                    )
                )
                + 2
            )  # adding a little extra space
            # set column width
            worksheet.set_column(idx, idx, max_len)

        # apply basic table format
        rows = len(df)
        cols = len(df.columns) - 1
        col_titles = []
        for c in df.columns:
            x = {"header": c}
            col_titles.append(x)
        worksheet.add_table(
            0,
            0,
            rows,
            cols,
            {
                "total_row": False,
                "columns": col_titles,
                "style": "Table Style Medium 2",
            },
        )




def format_excel_currency_white(filename, df, sheetname, range1, range2):
    """
    Function to auto fit the column widths and apply a table format style,
    when exporting excel sheets
    filename = output filename
    sheetname = Name to put on the excel sheet tab
    df = datframe to export to excel
    range of excel columns to format
    """
    # truncate sheetname - -excel will not accept >31
    sheetname = sheetname[:30]
    # load excelwriter class and set date formats
    with pd.ExcelWriter(
        filename,
        engine="xlsxwriter",
        date_format="DD/MM/YYYY",
        datetime_format="DD/MM/YYYY",
    ) as writer:

        # send df to writer
        df.to_excel(writer, sheet_name=sheetname, index=False)
        # get the workbook object
        workbook = writer.book
        # pull worksheet object
        worksheet = writer.sheets[sheetname]
        # set the formats
        currency = workbook.add_format({"num_format": "£#,##0"})
        percent = workbook.add_format({"num_format": "0%"})
        # percentage = workbook.add_format({'num_format':'0.00%'})
        if range1:
            worksheet.set_column(range1, None, currency)
        if range2:
            worksheet.set_column(range2, None, percent)

        # loop through all columns
        for idx, col in enumerate(df):
            series = df[col]
            # len of largest item
            max_len = (
                max(
                    (
                        series.astype(str).map(len).max(),
                        len(str(series.name)),  # len of column name/header
                    )
                )
                + 2
            )  # adding a little extra space
            # set column width
            worksheet.set_column(idx, idx, max_len)

        # apply basic table format
        rows = len(df)
        cols = len(df.columns) - 1
        col_titles = []
        for c in df.columns:
            x = {"header": c}
            col_titles.append(x)
        worksheet.add_table(
            0,
            0,
            rows,
            cols,
            {
                "total_row": False,
                "columns": col_titles,
                "style": "Table Style Light 1",
            },
        )

