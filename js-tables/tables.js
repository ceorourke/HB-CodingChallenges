$(document).ready(function(){
    $("#json-btn").click(function(){
        $.getJSON("CountryCodes.json", function(result){
            $.each(result, function(){
                $("#country-table").append(
                    "<tr><td>" + 
                    this.name + 
                    "</td><td>" + 
                    this.dial_code + 
                    "</td><td>" + 
                    this.code +
                    "</td></tr>" )
                console.log(this);
            });
        });
    });
});