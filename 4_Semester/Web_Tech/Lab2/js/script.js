// Get the button:
let mybutton = document.getElementById("myBtn");

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

const close = document.querySelector(".ad_close")

setInterval(function() {
  $('.overlay, .ad').fadeIn('slow');
  document.body.style.overflow = "hidden"
  setTimeout(function() {
    $('.ad_close').fadeIn('slow');
  }, 1500);
}, 60000);

$('.ad_close').on('click', function() {
    $('.overlay, .ad').fadeOut('slow');
    document.body.style.overflow = ""
  });



const cardData = [
    {
      title: 'Плед бавовняний',
      image: 'img/belgorod.jpg',
      price:  '500 грн',
      info: 'Бавовна (хлопок) – натуральна нитка рослинного походження. 🌱Відмінно пропускає повітря, не зігріває (ідеальний варіант для літа!), міцна, не утворює катишків і не вигорає на сонці.☀️ Дуже м’яка і практична пряжа☁️☁️☁️'

    },
    {
        title: 'Плед "Марс"',
        image: 'img/mars.jpg',
        price:  '550 грн',
        info: 'Акрил "Марс" складається з 90% акрилу і 10% мохеру. Мохер – тепла і практична пряжа. Її плетуть з вовни кіз, ворс досить довгий і пухнастий.🐐 Чудово зберігає тепло. Якщо прати таку пряжу в теплій воді з шампунем, то вироби довше залишаться пухнастими.☁️☁️☁️'

    },
    {
        title: 'Акриловий плед',
        image: 'img/akril.jpg',
        price:  '450 грн',
        info: 'Акрилова пряжа – тепла синтетична нитка. 🌝Сьогодні є дуже популярною завдяки своїй дешевизні і позитивним характеристикам.🥇Майже не скочується, приємна до тіла, відмінно зберігає тепло. Має велику кількість кольорів і відтінків.🌈'
    },
    {
        title: 'Плед "Напівбавовняний"',
        image: 'img/bnr.jpg',
        price:  '550 грн',
        info: 'Напіввовна (напівшерсть) складається з 50% акрилу та 50% вовни. 🐑Поєднує в собі властивості обох видів пряжі - приємна до тіла, відмінно зберігає тепло, не накопичує статичну електрику, не викликає алергічних реакцій (що в наш час дуже актуально), а груба шерсть практично не схильна до скочування. 🌟'
    },
    {
        title: 'Плед',
        image: 'img/lavanda.jpg',
        price:  '620 грн',
        info: ''
    },
    {
        title: 'Плед',
        image: 'img/rabbit.jpg',
        price:  '600 грн',
        info: ''
    },
    {
      title: 'Плед',
      image: 'img/1.jpg',
      price:  '450 грн',
      info: ''
  },
  {
      title: 'Плед',
      image: 'img/2.jpg',
      price:  '450 грн',
      info: ''
  },
  {
    title: 'Плед',
    image: 'img/3.jpg',
    price:  '500 грн',
    info: ''
  },
  {
    title: 'Плед',
    image: 'img/4.jpg',
    price:  '450 грн',
    info: ''
  },
  {
    title: 'Плед',
    image: 'img/5.jpg',
    price:  '550 грн',
    info: ''
  }

  ];

  console.log(cardData.length);

  const cardContainer = document.querySelector(".catalog");

  const initialLoadCount = 4;
  const loadMoreCount = 4;
  

  function displayCards(start, count) {
    
    cardData.slice(start, start + count).forEach(card => {
        let cardHTML = "";
        cardHTML += `
        <div class="card_wrapper">
                          <img src="${card.image}" alt="" class="card_img">
                          <card class="card_title">${card.title}</card>
                          <div class="card_price">${card.price}</div>
                          <div class="card_info" style="display:none">${card.info}</div>
                          <button class="show_info_button">Детальніше</button>
                          <button class="card_button">Купити</button>
                      </div>
        `;
      cardContainer.innerHTML += cardHTML;
    });
    
  }
    
  displayCards(0, initialLoadCount);
  
  function showInfo(){
  const showInfoButtons = document.getElementsByClassName("show_info_button");
  const infoContainers = document.getElementsByClassName("card_info");
  
  for (let i = 0; i < showInfoButtons.length; i++) {
    showInfoButtons[i].addEventListener('click', ()=> {
    const infoContainer=infoContainers[i] ; 
    infoContainer.style.display = "block";
  }
    );
  }
  }
  showInfo();
  const loadMoreButton = document.querySelector('.load_more_button');
  let loadedCount = initialLoadCount;
  
  loadMoreButton.addEventListener('click', () => {
    displayCards(loadedCount, loadMoreCount);
    loadedCount += loadMoreCount;
    console.log(loadedCount);
    if (loadedCount >= cardData.length){
      loadMoreButton.style.display = 'none';
    }
    showInfo();
  });

  
