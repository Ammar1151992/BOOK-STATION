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



// let carts = document.querySelectorAll('.box');
// for (let i = 0; i < carts.length; i++){
//   carts[i].addEventListener('click', () => {
//     cartNumber();
//   })
// }

// function onLoadCardNumber(){
//   let productNumber = localStorage.getItem('cartNumber');

//   if (productNumber){
//     document.querySelector('.bag .number0fcarts').textContent = productNumber;
//   }
// }

// function cartNumber(){
//   let productNumber = localStorage.getItem('cartNumber');
//   productNumber = parseInt(productNumber);

//   if (productNumber){
//     localStorage.setItem('cartNumber', productNumber + 1);
//     document.querySelector('.bag .number0fcarts').textContent = productNumber + 1;
//   } else{
//     localStorage.setItem('cartNumber', 1);
//     document.querySelector('.bag .number0fcarts').textContent = 1;
//   }
// }

// onLoadCardNumber();


let productInCart = JSON.parse(localStorage.getItem('ShoppingCart'));
if(!productInCart){
  productInCart=[];
}
const parentElement = document.querySelector('#buyItems');
const cartSumPrice = document.querySelector('#sum-prices');
const products = document.querySelectorAll('.box');



const countTheSumPrice = function(){
  let sumPrice = 0;
  productInCart.forEach(item => {
  sumPrice += item.price;
  });
  return sumPrice;
}

let checkout = []
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
    checkout = result
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
  console.log(item);
  item.addEventListener('click', (e) => {
    if (e.target.classList.contains('addCart')){
      const productID = e.target.dataset.productId;
      const productName = item.querySelector('.productName').innerHTML;
      const productPrice = item.querySelector('.priceValue').innerHTML;
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
  const isPlusButton = e.target.classList.contains('button-plus');0
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


var swiper = new Swiper(".mySwiper_flask", {

  breakpoints:{
    390:{
      slidesPerView:2,
      spaceBetween:10,
    },
    850:{
      slidesPerView:3,
      spaceBetween: 10,
    },
    1150:{
      slidesPerView:4,
      spaceBetween: 10,
    },
    1400:{
      slidesPerView:5,
      spaceBetween: 10,
    },
   
    1500:{
      slidesPerView:6,
      spaceBetween: 20,
    },
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
    
  },

  // pagination: {
  //   el: ".swiper-pagination",
  //   clickable: true,
  // },


  // And if we need scrollbar
  scrollbar: {
    el: '.swiper-scrollbar',
  },
  
});


var swiper = new Swiper(".mySwiper_home", {

  breakpoints:{
    390:{
      slidesPerView:3,
      spaceBetween: 10,
    },
    850:{
      slidesPerView:3,
      spaceBetween: 10,
    },
    1150:{
      slidesPerView:4,
      spaceBetween: 10,
    },
    1400:{
      slidesPerView:5,
      spaceBetween: 10,
    },
   
    1500:{
      slidesPerView:6,
      spaceBetween: 20,
    },
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
    
  },

  // pagination: {
  //   el: ".swiper-pagination",
  //   clickable: true,
  // },


  // And if we need scrollbar
  scrollbar: {
    el: '.swiper-scrollbar',
  },
  
});




var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}



function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}

  



//Get the button:
mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
