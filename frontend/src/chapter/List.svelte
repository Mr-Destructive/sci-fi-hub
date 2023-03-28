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
    return data.bookChapters;
  }

let chapters;
let bookId;
  onMount(async () => {
    if (token) {
      const apiUrl = 'http://localhost:8000/graphql/';
      let url = window.location.hash.split('/');
      bookId = url[url.length-1]
      let id = bookId
      if (parseInt(id) != id){
        url = new URLSearchParams(window.location.hash.split('?')[1]);
        bookId = url.get('bookId');
      }
      console.log(bookId)
      const query = `{bookChapters(bookId: ${bookId}){ id, name, order }}`;
      console.log(query)
      chapters = await fetchUserData(apiUrl, token, query);
    }
  });
</script>

{#if chapters }
    <ul>
    {#each chapters as chapter}
        <li>{chapter.order}<a href="/#/book/{bookId}/chapter/{chapter.order}">{chapter.name}</a></li>
    {/each}
    </ul>
{:else}
    <a href="/#/add/chapter/">
        <button>+ Chapter</button>
    </a>
{/if}
