<script>
  import { onMount } from 'svelte';
    import { getCookie } from '../utils';


  const token = getCookie('token');

  async function fetchUserData(apiUrl, token, query) {
    const resp = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ query })
    });

    const { data } = await resp.json();
    console.log(data)
    return data.book;
  }

let book;
let bookId;
  onMount(async () => {
    if (token) {
      const apiUrl = 'http://localhost:8000/graphql/';
      const url = window.location.href;
      let segment = url.split('/');
      bookId = segment[segment.length - 1];
      console.log(bookId)
      const query = `query{book(bookId:${bookId}){id, name, genre, author{username}}}`;
      book = await fetchUserData(apiUrl, token, query);
      console.log(book);
    }
  });
</script>

{#if book}
<p>
  {book.name} - By <i>"{book.author.username}"</i>
  {book.genre}
</p>
  <a href="/#/chapter/?bookId={book.id}"><button>+ Chapter</button></a>
{/if}

