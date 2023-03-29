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
    return data.books;
  }

let books = [];
  onMount(async () => {
    if (token) {
      const apiUrl = 'http://localhost:8000/graphql/';
      const query = 'query{books{id, name}}';
      books = await fetchUserData(apiUrl, token, query);
    }
  });
</script>

{#if books }
    <ul>
    {#each books as book}
        <li><a href="/#/book/{book.id}">{book.name}</a></li>
    {/each}
    </ul>

{:else}
  <p>Hello, Unauthenticated</p>
{/if}
   <a href='#/add/books/'><button>Add Book</button></a>
