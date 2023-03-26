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
    return data.books;
  }

let books = [];
  onMount(async () => {
    if (token) {
      const apiUrl = 'http://localhost:8000/graphql/';
      const query = 'query{books{id, name}}';
      books = await fetchUserData(apiUrl, token, query);
      console.log(books)
    }
  });
</script>

{#if books }
    <ul>
    {#each books as book}
        <li>{book.name}</li>
    {/each}
    </ul>

{:else}
  <p>Hello, Unauthenticated</p>
{/if}
   <button><a href='#/add/books/'>Add Book</a></button>
