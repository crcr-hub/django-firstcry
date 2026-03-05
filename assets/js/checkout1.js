

var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
$(document).ready(function(){


    $(".paywithcod").click(function(){
        console.log("clickedddd cod")
        var total = $('#total').val();
        var couponid = $('#cpnid').val();
        console.log(total)
        console.log("thishs",couponid)
        $.ajax({
            url:  "/order",
            type: 'POST',
            data: {
                'paymentmode':'CashOnDelivery',
                'cid':couponid,
                'total':total,
            },
            headers: {
                'X-CSRFToken': csrfToken
            },
            success: function(data) {
              
         
                // $('#msg').text('Operation successful');
             
                 console.log("success")
                 Swal.fire("congratulations!",data.status,"success").then((value) => {
                    window.location.href ="/orderhistory"
            });
              
             }

        });


    });






    $(".paywithRazor" ).click(function(e){ // click event to buttons with class 
        e.preventDefault();
        console.log("razor")
        var name = $("[name='name']").val();
        var hname =$("[name='house']").val();
        var street =$("[name='street']").val();
        var city =$("[name='city']").val();
        var state =$("[name='state']").val();
        var pin =$("[name='pin']").val();
        var mob =$("[name='mob']").val();
        var country = "India"
        var total_amount = $('#total_amount').val()
        var cid = $('#cid').val()
        console.log(name)
        var csrf_token = $("input[name=csrfmiddlewaretoken]").val();
        console.log("first one")
        $.ajax({
            method: "POST",
            url:"/paytoproceed",
            success: function(response){
                console.log("thisis response",response)
                var options = {
                    key: response.key,
                   amount: response.amount,
                    currency: "INR",
                    order_id: response.order_id,
                    "handler": function (res){
                        $.ajax({
                            method: "POST",
                            url: "/order/",
                             data: {
                            razorpay_payment_id: res.razorpay_payment_id,
                            razorpay_order_id: res.razorpay_order_id,
                            razorpay_signature: res.razorpay_signature,
                            csrfmiddlewaretoken: csrf_token
                            },
                            datatype: "datatype",
                            success: function(responsea){
                                Swal.fire("congratulations!",responsea.status,"success").then((value) => { 
                                    console.log("Test: Swal alert closed.");
                                        window.location.href ="/orderhistory"
                                });

                            }
                            
                        });
                       
                    },
                    "prefill": { //We recommend using the prefill parameter to auto-fill customer's contact information, especially their phone number
                        "name": name, //your customer's name
                        "email": "gaurav.kumar@example.com", 
                        //"contact": mob  //Provide the customer's phone number for better conversion rates 
                    },
                    
                    "theme": {
                        "color": "#3399cc"
                    }
                };
                var rzp1 = new Razorpay(options);
                rzp1.open();
            //     var rzp1 = new Razorpay(options);
            //         rzp1.on('payment.failed', function (res){
            //             console.log(total1)
            //             rzp1.close();
                        
                         
            //                 $.ajax({
                               
            //                     methos: "GET",
            //                     url: "/order",
            //                     data: {"paymentmode":"Pending",
            //                             "payment_id":res.razorpay_payment_id,
            //                             "total":total_amount,
            //                             'cid':cid,
            //                             },
            //                     datatype: "datatype",
            //                     success: function(respon){
                               
                                  
            //                         Swal.fire({
            //                             position: "top-end",
            //                             icon: "error",
            //                             title: "Your Order has been saved",
            //                             showConfirmButton: false,
            //                             timer: 2000, // Duration in milliseconds (1.5 seconds)
            //                             timerProgressBar: true // Show a progress bar
            //                         }).then(() => {
            //                             // Redirect to another page once the alert is closed
            //                             console.log("okkkk")
            //                             window.location.href = "/orderhistory";
            //                         })
            //                         console.log("failed2")
    
            //                     }
                                
            //                 });
                           
                         
  
            //         });
                   
            //             rzp1.open();
            //             e.preventDefault();
                    

            // } , 
            // error: function(xhr, status, error) {
            //     console.log("Request failed:");
            
             }
            
        });
    });       
});

