<script>
  import { onMount } from 'svelte';

  let user = null;

  const tokenCookie = localStorage.getItem('token');

  async function fetchUserData(apiUrl, token, query) {
    const resp = await fetch(apiUrl, {
      method: 'POST',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ query })
    });

    const { data } = await resp.json();
    return data.whoami;
  }

  onMount(async () => {
    if (tokenCookie) {
      const token = tokenCookie;
      const apiUrl = 'http://localhost:8000/graphql/';
      const query = '{whoami{id, username, email}}';
      user = await fetchUserData(apiUrl, token, query);
    }
  });
</script>

{#if user}
  <p>Hello, {user.username}</p>
{:else}
  <p>Hello, Unauthenticated</p>
{/if}
