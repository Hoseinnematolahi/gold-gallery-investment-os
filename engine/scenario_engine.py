def run_scenario(
    base_profit,
    scenario
):


    sales_factor = scenario["sales"]

    cost_factor = scenario["cost"]



    return (

        base_profit *
        sales_factor

        -
        cost_factor

    )
