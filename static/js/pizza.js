function addToCart(name) {
    let cartcookie = getCookie("cart");
    key = "cart";
    setCookie(key, cartcookie + "," + name, 365);
    console.log("added item '" + name + "' with key '" + key + "'");
    console.log(cartcookie);
    window.location.href = "/cart";
}
