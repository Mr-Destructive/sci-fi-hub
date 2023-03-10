<script>

    export let data = {};

    async function fetchData() {
        const apiUrl = 'http://localhost:8000/graphql/';
        const query = '{authors{id,username}}';
        const endpoint = `${apiUrl}?query=${encodeURIComponent(query)}`
        const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: 'query{authors{id,username}}' })
        });
        const result = await response.json();
        data = result.data;
  }

  fetchData();
</script>

{#if data.authors}
  <ul>
    {#each data.authors as author }
      <li>{author.username}</li>
    {/each}
  </ul>
{:else}
  <p>Loading...</p>
{/if}
