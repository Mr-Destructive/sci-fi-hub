<script>
  import { onMount } from 'svelte';
    import ListChapters from '../chapter/List.svelte';
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
      const query = `query{book(bookId:${bookId}){id, name, genre, author{username}}}`;
      book = await fetchUserData(apiUrl, token, query);
    }
  });
</script>

{#if book}

  <h2>
    {book.name}
  </h2>
  <h3>- By <i>"{book.author.username}"</i></h3>
  {book.genre}
  <a href="/#/add/chapter/?bookId={bookId}"><button>+ Chapter</button></a>
  <p>
    <ListChapters bind:bookId={book.id}/>
  </p>
{/if}

