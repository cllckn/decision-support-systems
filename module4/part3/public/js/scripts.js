$(function () {
    // Login button click event
    $(document).on("click", "#loginBtn", () => {
        const username = $("#username").val();
        const password = $("#password").val();

        $.ajax({
            url: "/login",
            method: "POST",
            contentType: "application/json",
            data: JSON.stringify({ username, password }),
            success: (response) => {
                localStorage.setItem("token", response.token);

                // Decode token and redirect based on role
                try {
                    const decoded = jwt_decode(response.token);
                    const role = decoded.role;

                    switch (role) {
                        case 1:
                            window.location.href = "dashboard.html";
                            break;
                        case 2:
                            window.location.href = "registered-user.html";
                            break;
                        default:
                            window.location.href = "unauthorized.html";
                    }
                } catch (error) {
                    console.error("Token decoding failed:", error);
                    window.location.href = "unauthorized.html";
                }
            },
            error: () => {
                $("#errorMsg").text("Invalid credentials").removeClass("hidden");
            }
        });
    });

    // Dashboard or Registered User Page Access Control
    if (["/dashboard.html", "/registered-user.html"].some(path => window.location.pathname.includes(path))) {
        const token = localStorage.getItem("token");

        if (!token) {
            window.location.href = "unauthorized.html";
            return;
        }

        // Logout button functionality (both sidebar and main content)
        function logout() {
            localStorage.removeItem("token");
            window.location.href = "login.html";
        }

        $("#logoutBtn, #logoutSidebarBtn").click(() => {
            if (confirm("Are you sure you want to log out?")) {
                logout();
            }
        });

        // Fetch Customer List
        $("#customerListBtn").click(function () {
            $.ajax({
                url: "http://localhost:3000/api/customers",
                method: "GET",
                headers: { Authorization: `Bearer ${token}` },
                success: function (data) {
                    $("#customerListContainer").removeClass("hidden");
                    const customerTableBody = $("#customerListBody");
                    customerTableBody.empty();

                    data.forEach(customer => {
                        customerTableBody.append(`
                            <tr>
                                <td class="border border-gray-300 px-4 py-2">${customer.id}</td>
                                <td class="border border-gray-300 px-4 py-2">${customer.name}</td>
                                <td class="border border-gray-300 px-4 py-2">${customer.email}</td>
                                <td class="border border-gray-300 px-4 py-2">${customer.phone}</td>
                                <td class="border border-gray-300 px-4 py-2">${customer.city}</td>
                            </tr>
                        `);
                    });
                },
                error: function (xhr) {
                    if (xhr.status === 403) {
                        alert("Access denied! Only admins can view customer data.");
                    } else if (xhr.status === 401) {
                        alert("Unauthorized! Please log in again.");
                        window.location.href = "login.html"; // Redirect to login
                    } else {
                        alert("Failed to fetch customers. Please try again.");
                    }
                }
            });
        });
    }
});
