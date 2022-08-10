
import webbrowser

meniu_restaurant = open("meniu.html", "w")
html_content = """
    <html>
    
    <head>
            <h1 style="text-align:center;font-family:verdana">Restaurantul IT</h1>
    </head>

    <body style="background-color:powderblue">
            <h2 style="color:dodgerblue;text-align:center;font-size:160%"><u>Meniu</u></h2>
    <hr>
    <p style="text-align:center"><b>Ciorbe</b></p>
    <ol>
        <p>Ciorba de burta .................................................................... 15 lei</p>
        <p>Ciorba de legume ................................................................ 10 lei</p>
        <p>Ciorba de porc a la grec ...................................................... 14 lei</p>
        <p>Supa de pui ......................................................................... 12 lei</p>
    </ol>
    <hr>
    <p style="text-align:center"><b>Fel principal</b></p>
   <ol>
        <p>Snitel de porc cu piure de conopida si sos de merisoare ................................................................................... 35 lei</p>
        <p>Biban de mare cu spanac, usturoi si migdale insotit de cartofi cu usturoi si patrunjel ...................................... 60 lei</p>
        <p>Somon cu orez prajit .......................................................................................................................................... 66 lei</p>
        <p>Burger din antricot de vita alaturi de cartofi prajiti in untura de vita ................................................................. 59 lei</p>
    </ol>
    <hr>
    <p style="text-align:center"><b>Desert</b></p>
    <ol>
        <p>Tarta cu visine ................................................................................... 12 lei</p>
        <p>Cheesecake cu biscuiti Oreo ............................................................. 12 lei</p>
        <p>Papanasi cu ciocolata sau gem din fructe de padure ......................... 14 lei</p>
        <p>Clatite cu dulceata din cirese amare si frisca .................................... 13 lei</p>
    </ol>
    <hr>
    <p style="text-align:center"><b><i>Pofta buna ;)<b></i></p>
    
    </body>
    </html>
    """

meniu_restaurant.write(html_content)

meniu_restaurant.close()

webbrowser.open("meniu.html")
