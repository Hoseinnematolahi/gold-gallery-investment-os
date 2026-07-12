
def inventory_value(
    gram,
    price
):

    return gram * price



def calculate_revenue(
    sales_gram,
    gold_price,
    making_fee
):

    gold_value = (
        sales_gram *
        gold_price
    )


    making_income = (
        gold_value *
        making_fee
    )


    return (
        gold_value +
        making_income
    )



def calculate_profit(
    revenue,
    cost
):

    return revenue-cost



def calculate_roi(
    annual_profit,
    investment
):

    if investment==0:
        return 0


    return (
        annual_profit /
        investment
    )*100



def calculate_payback(
    investment,
    monthly_profit
):

    if monthly_profit<=0:
        return None


    return (
        investment /
        monthly_profit
    )
