
 let input_service = document.getElementById("service");
 let button = document.getElementById("submit");

    document.addEventListener("DOMContentLoaded", (e) => {      
        button.disabled = true;              
    });
    
    input_service.addEventListener("change", stateHandle);     

    function stateHandle() {
        service = document.getElementById("service");
        service[0].innerText = "Choose the service";
        barber = document.getElementById("barber");
        working_days = document.getElementById("working_days");
        barber.selectedIndex = 0;
        working_days.selectedIndex = 0;
        button.disabled = true; 
    }

    
   

  