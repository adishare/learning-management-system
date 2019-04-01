function openTabs(evt, opsi){
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    for(i=0;i<tabcontent.length;i++){
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablink");
    for(i=0;i<tablinks.length;i++){
        tablinks[i].className = tablinks[i].className.replace("active", "");
    }

    document.getElementById(opsi).style.display = "block";
    evt.currentTarget.className += "active";
}
