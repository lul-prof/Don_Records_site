function scrollToSection(sectionId) {
  alert(`You clicked ${sectionId} — Implement scroll logic here`);
}
document.addEventListener('DOMContentLoaded', function() {
  const scrollLinks = document.querySelectorAll('.scroll-link');
  scrollLinks.forEach(link => {
    link.addEventListener('click', function(event) {
      event.preventDefault();
      const sectionId = this.getAttribute('href').substring(1);
      scrollToSection(sectionId);
    });
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".beat-card button");

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      const beatName = button.parentElement.querySelector("p").innerText;

      // Simulate purchase confirmation
      showToast(`${beatName} added to cart!`);

      // Optionally, redirect to checkout
      // window.location.href = '/checkout';
    });
  });
});

// Toast alert popup
function showToast(message) {
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.innerText = message;
  document.body.appendChild(toast);

  setTimeout(() => {
    toast.classList.add("show");
  }, 100);

  setTimeout(() => {
    toast.classList.remove("show");
    setTimeout(() => document.body.removeChild(toast), 300);
  }, 2500);
}


// === Shopping Cart Drawer & LocalStorage ===
document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".beat-card button");
  const cartDrawer = document.getElementById("cart-drawer");
  const cartItemsContainer = document.getElementById("cart-items");
  const openCartBtn = document.getElementById("open-cart");
  const closeCartBtn = document.getElementById("close-cart");

  const cart = JSON.parse(localStorage.getItem("beatCart")) || [];

  function updateCartDrawer() {
    cartItemsContainer.innerHTML = "";
    cart.forEach((item, i) => {
      const el = document.createElement("div");
      el.className = "cart-item";
      el.innerHTML = `
        <span>${item}</span>
        <button data-index="${i}" class="remove-btn">✕</button>
      `;
      cartItemsContainer.appendChild(el);
    });
    localStorage.setItem("beatCart", JSON.stringify(cart));
  }

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      const beatName = button.parentElement.querySelector("p").innerText;
      cart.push(beatName);
      updateCartDrawer();
      showToast(`${beatName} added to cart!`);
    });
  });

  openCartBtn.onclick = () => cartDrawer.classList.add("visible");
  closeCartBtn.onclick = () => cartDrawer.classList.remove("visible");

  cartItemsContainer.addEventListener("click", (e) => {
    if (e.target.classList.contains("remove-btn")) {
      const index = e.target.dataset.index;
      cart.splice(index, 1);
      updateCartDrawer();
    }
  });

  updateCartDrawer();
});

function showToast(message) {
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.innerText = message;
  document.body.appendChild(toast);
  setTimeout(() => toast.classList.add("show"), 100);
  setTimeout(() => toast.classList.remove("show"), 2500);
  setTimeout(() => toast.remove(), 2800);
}

// === Audio Visualizer ===
window.addEventListener("load", () => {
  document.querySelectorAll(".beat-card audio").forEach(audio => {
    const canvas = document.createElement("canvas");
    canvas.className = "visualizer";
    audio.parentElement.appendChild(canvas);

    const ctx = canvas.getContext("2d");
    canvas.width = 150;
    canvas.height = 40;

    const context = new AudioContext();
    const analyser = context.createAnalyser();
    const source = context.createMediaElementSource(audio);
    source.connect(analyser);
    analyser.connect(context.destination);
    analyser.fftSize = 64;

    const bufferLength = analyser.frequencyBinCount;
    const dataArray = new Uint8Array(bufferLength);

    function draw() {
      requestAnimationFrame(draw);
      analyser.getByteFrequencyData(dataArray);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const barWidth = canvas.width / bufferLength;

      for (let i = 0; i < bufferLength; i++) {
        const barHeight = dataArray[i] / 2;
        ctx.fillStyle = `rgb(${barHeight + 100}, 50, 150)`;
        ctx.fillRect(i * barWidth, canvas.height - barHeight, barWidth - 1, barHeight);
      }
    }
    draw();
  });
});


document.addEventListener('DOMContentLoaded', () => {
  const cartButton = document.getElementById('cart-button');
  const cartDrawer = document.getElementById('cart-drawer');
  const closeCart = document.getElementById('close-cart');
  const cartItems = document.getElementById('cart-items');
  const cartCount = document.getElementById('cart-count');
  const toast = document.getElementById('toast');

  // Load cart from localStorage
  let cart = JSON.parse(localStorage.getItem('cart')) || [];

  function saveCart() {
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartUI();
  }

  function updateCartUI() {
    cartItems.innerHTML = '';
    cart.forEach((item, index) => {
      const div = document.createElement('div');
      div.className = 'cart-item';
      div.innerHTML = `
        <span>${item.name}</span>
        <span>$${item.price}</span>
        <button onclick="removeItem(${index})">❌</button>
      `;
      cartItems.appendChild(div);
    });
    cartCount.textContent = cart.length;
  }

  // Make remove function global
  window.removeItem = (index) => {
    cart.splice(index, 1);
    saveCart();
  };

  // Add to cart
  document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', () => {
      const name = button.getAttribute('data-name');
      const price = button.getAttribute('data-price');
      cart.push({ name, price });
      saveCart();

      toast.textContent = `${name} added to cart`;
      toast.classList.remove('hidden');
      setTimeout(() => toast.classList.add('hidden'), 3000);
    });
  });

  // Toggle cart drawer
  cartButton.addEventListener('click', () => {
    cartDrawer.classList.toggle('open');
  });

  closeCart.addEventListener('click', () => {
    cartDrawer.classList.remove('open');
  });

  // Initial render
  updateCartUI();
});

document.addEventListener('DOMContentLoaded', function () {
  const cart = [];
  const cartButton = document.getElementById('cart-button');
  const cartDrawer = document.getElementById('cart-drawer');
  const closeCart = document.getElementById('close-cart');
  const cartItemsContainer = document.getElementById('cart-items');
  const cartCount = document.getElementById('cart-count');
  const toast = document.getElementById('toast');

  // Show cart drawer
  cartButton.addEventListener('click', () => {
    cartDrawer.classList.add('open');
  });

  // Hide cart drawer
  closeCart.addEventListener('click', () => {
    cartDrawer.classList.remove('open');
  });

  // Add to cart
  document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', () => {
      const name = button.getAttribute('data-name');
      const price = button.getAttribute('data-price');

      cart.push({ name, price });
      updateCartUI();
      showToast(`${name} added to cart`);
    });
  });

  function updateCartUI() {
    cartItemsContainer.innerHTML = '';
    cart.forEach((item, index) => {
      const div = document.createElement('div');
      div.classList.add('cart-item');
      div.innerHTML = `<p>${item.name} - $${item.price}</p>`;
      cartItemsContainer.appendChild(div);
    });
    cartCount.textContent = cart.length;
  }

  function showToast(message) {
    toast.textContent = message;
    toast.classList.remove('hidden');
    toast.classList.add('visible');

    setTimeout(() => {
      toast.classList.remove('visible');
      toast.classList.add('hidden');
    }, 3000);
  }
});
