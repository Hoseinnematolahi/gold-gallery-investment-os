{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
def inventory_value(\
    gram,\
    price\
):\
\
    return gram * price\
\
\
\
def calculate_revenue(\
    sales_gram,\
    gold_price,\
    making_fee\
):\
\
    gold_value = (\
        sales_gram *\
        gold_price\
    )\
\
\
    making_income = (\
        gold_value *\
        making_fee\
    )\
\
\
    return (\
        gold_value +\
        making_income\
    )\
\
\
\
def calculate_profit(\
    revenue,\
    cost\
):\
\
    return revenue-cost\
\
\
\
def calculate_roi(\
    annual_profit,\
    investment\
):\
\
    if investment==0:\
        return 0\
\
\
    return (\
        annual_profit /\
        investment\
    )*100\
\
\
\
def calculate_payback(\
    investment,\
    monthly_profit\
):\
\
    if monthly_profit<=0:\
        return None\
\
\
    return (\
        investment /\
        monthly_profit\
    )}