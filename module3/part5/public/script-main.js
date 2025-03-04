$(document).ready(function() {
    $("#content-area").load("home.html");

    $("#home-link").click(function(event) {
        event.preventDefault();
        $("#content-area").load("home.html");
    });

    $("#products-link").click(function(event) {
        event.preventDefault();
        $("#content-area").load("products.html", function() {
            loadProducts();
        });
    });

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
                                <tr>
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

});
