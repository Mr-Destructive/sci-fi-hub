<script>
  import { onMount } from 'svelte';
  import { getCookie } from '../utils';
  export let bookId;

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
    return data.bookChapters;
  }

let chapters;
  onMount(async () => {
    if (token) {
      const apiUrl = 'http://localhost:8000/graphql/';
      const query = `{bookChapters(bookId: ${bookId}){ id, name, order }}`;
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
