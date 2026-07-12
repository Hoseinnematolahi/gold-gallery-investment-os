def optimize_mix(
    inventory,
    products
):


    result={}


    for key,item in products.items():


        gram = (
            inventory *
            item["default_share"]
            /
            100
        )


        profit = (

            gram *
            item["margin"]

        )


        result[key]={

            "gram":round(gram),

            "profit_score":
            round(profit,2)

        }


    return result
