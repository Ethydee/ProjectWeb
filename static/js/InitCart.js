function cart() {
    let cartlist = document.getElementById("CartList");
    splitcookie = getCookie("cart").slice(1).split(",");
    console.log(splitcookie);
    if (splitcookie[0] === "") {
        splitcookie = [];
    }
    for (item in splitcookie) {
        item = splitcookie[item];
        cartlist.innerHTML += `<li><h3>${item}</h3></li>`;
    }
    if (splitcookie.length === 0) {
        cartlist.innerHTML = "<h1>Cart is Empty.</h1>";
    }
}

function order() {
    setCookie("cart", "", 365);
    document.getElementById("CartList").innerHTML = `<h1 style="color: green">Thanks For Your Order!</h1>`;
}

$(document).ready(function() {
    cart();
    console.log("ready!");
});
