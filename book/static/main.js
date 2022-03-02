const currentLocation = location.href;
const menuItem = document.querySelectorAll('a');
const menuLength = menuItem.length;
for (let i = 0; i < menuLength; i++) {
  if (menuItem[i].href === currentLocation) {
    menuItem[i].className = "active"
  }
}

var swiper = new Swiper(".mySwiper", {
  loop: true,
  autoplay: {
    delay: 3000,
  },
  pagination: {
    el: ".swiper-pagination",
  },
});


  

var swiper = new Swiper(".mySwiper_release", {
  // Optional parameters
  
  loop: true,
  slidesPerView: 5,
  spaceBetween: 5,
  slidesPerView : 'auto',
  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
    
  },


  // And if we need scrollbar
  scrollbar: {
    el: '.swiper-scrollbar',
  },
  
});



let carts = document.querySelectorAll('.product');
for (let i = 0; i < carts.length; i++){
  carts[i].addEventListener('click', () => {
    cartNumber();
  })
}

function onLoadCardNumber(){
  let productNumber = localStorage.getItem('cartNumber');

  if (productNumber){
    document.querySelector('.bag .number0fcarts').textContent = productNumber;
  }
}

function cartNumber(){
  let productNumber = localStorage.getItem('cartNumber');
  productNumber = parseInt(productNumber);

  if (productNumber){
    localStorage.setItem('cartNumber', productNumber + 1);
    document.querySelector('.bag .number0fcarts').textContent = productNumber + 1;
  } else{
    localStorage.setItem('cartNumber', 1);
    document.querySelector('.bag .number0fcarts').textContent = 1;
  }
}

onLoadCardNumber();


let productInCart = JSON.parse(localStorage.getItem('ShoppingCart'));
if(!productInCart){
  productInCart=[];
}
const parentElement = document.querySelector('#buyItems');
const cartSumPrice = document.querySelector('#sum-prices');
const products = document.querySelectorAll('.product');



const countTheSumPrice = function(){
  let sumPrice = 0;
  productInCart.forEach(item => {
  sumPrice += item.price;
  });
  return sumPrice;
}

const updateShoppingCartHTML = function(){
  localStorage.setItem('ShoppingCart', JSON.stringify(productInCart))
  if (productInCart.length > 0){
    let result = productInCart.map(product => {
      return `
       <li class="buyItem">
            <img src="${product.image}">
            <div>
                <h5>${product.name}</h5>
                <h6>IQD${product.price}</h6>
                <div>
                    <button class="button-minus" data-id=${product.id}>-</button>
                    <span class="countOfProduct">${product.count}</span>
                    <button class="button-plus" data-id=${product.id}>+</button>
                </div>
            </div>
        </li>`
    });

    parentElement.innerHTML = result.join('');
    document.querySelector('.checkout').classList.remove('hidden')
    cartSumPrice.innerHTML= "المجوع: " + "IQD" + countTheSumPrice();
  } else{
    document.querySelector('.checkout').classList.add('hidden')
    parentElement.innerHTML = '<h4 class="empty">عربة التسوق فارغة</h4>';
    cartSumPrice.innerHTML="";
  }
}

function updateProductInCart(product){
  for (let i = 0; i < productInCart.length; i++){
    if (productInCart[i].id == product.id){
        productInCart[i].count += 1;
        productInCart[i].price = productInCart[i].basePrice * productInCart[i].count;
        return;
    }
  }
  productInCart.push(product);
}

products.forEach(item => {
  item.addEventListener('click', (e) => {
    if (e.target.classList.contains('addToCart')){
      const productID = e.target.dataset.productId;
      const productName = item.querySelector('.silders_des').innerHTML;
      const productPrice = item.querySelector('.silders_price').innerHTML;
      const productImage = item.querySelector('img').src;
      let product = {
        name: productName,
        image: productImage,
        id: productID,
        count: 1,
        price: parseInt(productPrice),
        basePrice: parseInt(productPrice)
      }
      updateProductInCart(product);
      updateShoppingCartHTML();
    }
  });
});


parentElement.addEventListener('click', (e) =>{
  const isPlusButton = e.target.classList.contains('button-plus');
  const isMinusButton = e.target.classList.contains('button-minus');
  if (isPlusButton || isMinusButton){
    for (let i = 0; i < productInCart.length; i++){
      if(productInCart[i].id === e.target.dataset.id){
        if(isPlusButton){
          productInCart[i].count += 1
        }
        else if(isMinusButton){
          productInCart[i].count -= 1
        }
        productInCart[i].price = productInCart[i].basePrice * productInCart[i].count;
      }
      if(productInCart[i].count <= 0){
        productInCart.splice(i, 1);
      }
    }
    updateShoppingCartHTML();
  }
});


updateShoppingCartHTML();

const openShopCart = document.querySelector('.shoppingCartButton');
openShopCart.addEventListener('click', () => {
	const cart = document.querySelector('.producstOnCart');
	cart.classList.toggle('hide');
	document.querySelector('body').classList.toggle('stopScrolling');
});

function closeCart() {
	const cart = document.querySelector('.producstOnCart');
	cart.classList.toggle('hide');
	document.querySelector('body').classList.toggle('stopScrolling')
}


const closeShopCart = document.querySelector('#closeButton');
const overlay = document.querySelector('.overlay_4');
closeShopCart.addEventListener('click', closeCart);
overlay.addEventListener('click', closeCart);


// const responsiveNavbar = (function () {
// 	const button = document.querySelector("#menuButton");
// 	const navbar = document.querySelector("#navbar")
// 	button.addEventListener("click", function () {
// 		if (navbar.className === "navbar") {
// 			navbar.className += " navbarResponsive";
// 		}
// 		else {
// 			navbar.className = "navbar";
// 		}
// 	});
// })();

// if (document.getElementById('hearderSlide')) {
// 	$('#hearderSlide').multislider();
// 	$('#hearderSlide').multislider('pause');
// }


// function closeCart() {
// 	const cart = document.querySelector('.producstOnCart');
// 	cart.classList.toggle('hide');
// 	document.querySelector('body').classList.toggle('stopScrolling')
// }


// const openShopCart = document.querySelector('.shoppingCartButton');
// openShopCart.addEventListener('click', () => {
// 	const cart = document.querySelector('.producstOnCart');
// 	cart.classList.toggle('hide');
// 	document.querySelector('body').classList.toggle('stopScrolling');
// });


// const closeShopCart = document.querySelector('#closeButton');
// const overlay = document.querySelector('.overlay');
// closeShopCart.addEventListener('click', closeCart);
// overlay.addEventListener('click', closeCart);

