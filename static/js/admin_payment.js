// document.addEventListener("DOMContentLoaded", function () {
//     const orderSelect = document.getElementById("id_order");
//     const amountField = document.getElementById("id_amount");

//     if (orderSelect) {
//         orderSelect.addEventListener("change", function () {
//             const orderId = orderSelect.value;

//             if (orderId) {
//                 fetch(`/api/restaurant/orders/${orderId}/total_amount/`)
//                     .then(response => response.json())
//                     .then(data => {
//                         amountField.value = data.total_amount;
//                     });
//             }
//         });
//     }
// });

document.addEventListener("DOMContentLoaded", function () {
    const orderSelect = document.getElementById("id_order");
    const amountField = document.getElementById("id_amount");

    if (orderSelect) {
        orderSelect.addEventListener("change", function () {
            const orderId = orderSelect.value;

            if (orderId) {
                fetch(`/api/restaurant/orders/${orderId}/total_amount/`)  
                    .then(response => response.json())
                    .then(data => {
                        if (data.total_amount !== undefined) {
                            amountField.value = data.total_amount;
                        } else {
                            alert("Erreur lors de la récupération du montant total.");
                        }
                    })
                    .catch(error => console.error("Erreur lors de la récupération du montant total:", error));
            }
        });
    }
});


// (function ($) {
//     $(document).ready(function () {
//         $('#id_discount, #id_order').change(function () {
//             const discountId = $('#id_discount').val();
//             const orderId = $('#id_order').val();

//             if (orderId) {
//                 $.ajax({
//                     url: `/api/restaurant/calculate-payment-amount/`,  
//                     data: {
//                         'discount_id': discountId,
//                         'order_id': orderId
//                     },
//                     success: function (response) {
//                         $('#id_amount').val(response.amount);
//                     }
//                 });
//             }
//         });
//     });
// })(django.jQuery);

// (function ($) {
//     $(document).ready(function () {
//         $('#id_discount, #id_order').change(function () {
//             const discountId = $('#id_discount').val();
//             const orderId = $('#id_order').val();

//             if (orderId) {
//                 $.ajax({
//                     url: `/api/restaurant/calculate-payment-amount/`,  
//                     data: {
//                         'discount_id': discountId,
//                         'order_id': orderId
//                     },
//                     success: function (response) {
//                         if (response.amount !== undefined) {
//                             $('#id_amount').val(response.amount);
//                         } else {
//                             alert("Erreur lors de la récupération du montant après remise.");
//                         }
//                     },
//                     error: function (xhr, status, error) {
//                         console.error("Erreur lors du calcul du montant après remise:", error);
//                     }
//                 });
//             }
//         });
//     });
// })(django.jQuery);