$(document).ready(function () {
  const SERVER_URL = "http://localhost:4000/client/products";

  // Fetch and display posts
  function loadPosts() {
    $.get(SERVER_URL, function (products) {
      //alert(JSON.stringify(products));
      $("#productsTable").empty();
      products.forEach(product => {
        $("#productsTable").append(`
                    <tr class="border border-gray-300">
                        <td class="border border-gray-300 p-2">${product.id}</td>
                        <td class="border border-gray-300 p-2">${product.name}</td>
                         <td class="border border-gray-300 p-2">${product.price}</td>
                    </tr>
                `);
      });
    });
  }

  loadPosts(); // Load posts on page load

  // Handle new post submission
  $("#postForm").submit(function (event) {
    event.preventDefault();

    const newProducts = {
      name: $("#name").val(),
      price: $("#price").val()
    };

    //alert(JSON.stringify(newProducts));

    $.post(SERVER_URL, newProducts, function (response) {
      alert("Product added successfully!");
      loadPosts(); // Refresh posts list
      $("#postForm")[0].reset(); // Clear form
    });
    // Asynchronous request to add a product
    $.post({
      url: SERVER_URL,
      contentType: "application/json", // Ensure JSON is sent correctly
      data: JSON.stringify(newProducts),
      success: function(response) {
        loadPosts(); // Refresh products list
        $("#postForm")[0].reset(); // Clear form
      },
      error: function(xhr) {
        console.error("Error:", xhr.responseText);
      }
    });

  });
});
