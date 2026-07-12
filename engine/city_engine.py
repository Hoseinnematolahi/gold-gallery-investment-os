cities={


"شیراز":
{

"market":90,
"competition":80,
"rent":70

},


"اهواز":
{

"market":75,
"competition":65,
"rent":55

},


"مرودشت":
{

"market":55,
"competition":40,
"rent":35

},


"ارسنجان":
{

"market":40,
"competition":30,
"rent":20

}

}



def city_score(city):


    data=cities[city]


    return (

        data["market"]*0.5

        -

        data["competition"]*0.3

        -

        data["rent"]*0.2

    )
