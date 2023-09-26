
 let input_service = document.getElementById("service");
 let button = document.getElementById("submit");

    document.addEventListener("DOMContentLoaded", (e) => {      
        button.disabled = true;              
    });
    
    input_service.addEventListener("change", stateHandle);     

    function stateHandle() {
        service = document.getElementById("service");
        barber = document.getElementById("barber");
        working_days = document.getElementById("working_days");
        barber.selectedIndex = 0;
        working_days.selectedIndex = 0; 

        if(service.selectedIndex > 0 && barber.selectedIndex > 0 
            && working_days.selectedIndex > 0 )  {            
            button.disabled = false; 
        } 
        else {
            button.disabled = true;
        }
    }

    
   

  