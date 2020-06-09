<script>
	import { onMount, onDestroy } from 'svelte';
    import Cookies from 'js-cookie/src/js.cookie.js';

    let books = [];

    function getRef(id) {return document.getElementById(id).href;};


    const CSRF_TOKEN = Cookies.get('csrftoken');
    const SHOP_URL = getRef("shop-ref");
    onMount(async () => {
       const response = await fetch(SHOP_URL,  {
                                     headers: {
                                        'Accept': 'application/json, text-plain, */*',
                                        'X-Requested-With': 'XMLHttpRequest',
                                     }, });

       let book_json = await response.json();
        books = book_json['books']
        books = books
       console.log(books)
   });


function onInterval(callback, ms) {
        const interval = setInterval(callback, ms);

        onDestroy(() => {
            clearInterval(interval);
        });
    }


let socket = new WebSocket("ws://localhost:8000");
socket.onopen = function(e) {
    console.log("[open] Соединение установлено");
    console.log("C");
    socket.send("books?");
    onInterval(async () => {
        socket.send("books?");
    }, 1000);
};

socket.onmessage = function(event) {
  console.log(`[message] Данные получены с сервера: ${event.data}`);
  let value = JSON.parse(event.data)['value'];
  document.getElementById("book-count").innerText = value;

};


</script>


<main>
     <section class="static about-sec">
        <div class="container">
            <h2>recently added books to our store</h2>
            <div class="recent-book-sec">
                <div class="row">

                    {#each books as item }
                    <div class="col-md-3">
                        <div class="item">
                            <a href="."><img src="../static/{item.image}" alt="img">
                <!--						background-image:{'url(/static/shop/' + item.img + ')'}-->
                            <h6>{item.author}</h6>
                            <h6>{item.name}</h6></a>
                            <h6><span class="price">{item.discount}</span> / <a href=".">Buy Now</a></h6>
                        </div>
                    </div>
                    {/each}

                </div>
                <div class="btn-sec">
                    <button class="btn gray-btn">load More books</button>
                </div>
            </div>
        </div>
    </section>

</main>
<style>

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>