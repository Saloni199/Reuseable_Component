*** Settings ***
Documentation       Template robot main suite.

Library             YASH.Tabula
Library             RPA.Tables
Library             RPA.Excel.Application
Library             RPA.Excel.Files


*** Tasks ***
Minimal task
    ${Table}=    Get Table    1710.05006.pdf    0
    Log    ${Table}

    ${Table1}=    Get All Tables    1710.05006.pdf
    Log    ${Table1}

    ${Table2}=    Get Table On Page At Index    1710.05006.pdf    2    1
    Log    ${Table2}
