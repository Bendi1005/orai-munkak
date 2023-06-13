function kalkulal(){
    //Űrlapadatok
    const szelesseg=document.getElementById('szelesseg');
    const magassag=document.getElementById('magassag');
    const papir=document.getElementById('papirtipus').value;
    //Számítások
    let terulet=Math.round((szelesseg*magassag)/10000);    
    let koltseg=terulet*papir;
    //Megjelenítés
    document.getElementById('valasz').style.visibility = "visible";
    document.getElementById('koltseg').innerHTML = koltseg;
}

