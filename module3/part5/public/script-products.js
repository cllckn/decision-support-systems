$(document).ready(function() {

    let debounceTimer;

    function loadProducts(query = "") {
        let url = query ? `/api/products?name=${encodeURIComponent(query)}` : "/api/products";
        $.get(url, function(products){
            $("#product-list").empty();
            if (products.length === 0) {
                $("#search-error").show();
            } else {
                $("#search-error").hide();
                products.forEach(product => {
                    $("#product-list").append(`
                                <tr >
                                    <td>${product.id}</td>
                                    <td>${product.name}</td>
                                    <td>${product.price}</td>
                                    <td>
                                        <button data-id="${product.id}"  class="edit-btn focus:outline-none text-white bg-yellow-400 hover:bg-yellow-500 focus:ring-4 focus:ring-yellow-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:focus:ring-yellow-900">Update</button>
                                        <button data-id="${product.id}" class="delete-btn focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-900">Delete</button>

                                    </td>
                                </tr>
                            `);
                });
            }
        });
    }



    $("#add-product-form").submit(function(event){
        event.preventDefault();
        let name = $("#name").val().trim();
        let price = parseFloat($("#price").val().trim());

        if (!name || isNaN(price) || price <= 0) {
            $("#error-msg").fadeIn().delay(5000).fadeOut();
            return;
        }

        $.post({
            url: "/api/products",
            contentType: "application/json",
            data: JSON.stringify({ name, price }),
            success: function() {
                loadProducts();
                $("#name, #price").val("");
            }
        });
    });

    $("#product-list").on("click", ".delete-btn", function() {
        let id = $(this).data("id");
        $.ajax({
            url: `/api/products/${id}`,
            type: "DELETE",
            success: function() {
                loadProducts();
            }
        });
    });

    // Live search with API request and debouncing
    $("#search").on("keyup", function() { // attaches an event listener to the search input field (#search). The event triggers whenever the user releases a key (keyup event).
        clearTimeout(debounceTimer); // Clears any previously set timer (debounceTimer) to prevent multiple requests being sent in quick succession.
        let query = $(this).val().trim();
        debounceTimer = setTimeout(() => { //Sets a delay of 300 milliseconds before calling loadProducts(query).
            loadProducts(query);
        }, 300);
    });

    $("#update-product-form").submit(function(event){
        event.preventDefault();
        let id = parseInt($("#update-id").val().trim());
        let name = $("#update-name").val().trim();
        let price = parseFloat($("#update-price").val().trim());

        if (isNaN(id) || id <= 0 || (!name && isNaN(price))) {
            $("#update-error-msg").fadeIn().delay(5000).fadeOut();
            return;
        }

        $.ajax({
            url: `/api/products/${id}`,
            type: "PUT",
            contentType: "application/json",
            data: JSON.stringify({ name, price }),
            success: function() {
                loadProducts();
                $("#update-id, #update-name, #update-price").val("");
            }
        });
    });

    // Load product data into update form when "Edit" is clicked
    $("#product-list").on("click", ".edit-btn", function() {
        let id = $(this).data("id");
        $("#updateform").fadeIn(2000);
        $.get(`/api/products/${id}`, function(product) {
            $("#update-id").val(product.id);
            $("#update-name").val(product.name);
            $("#update-price").val(product.price);
        });
    });
});
