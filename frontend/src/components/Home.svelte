<script>
    import jwtDecode from 'jwt-decode';
  import { onMount } from 'svelte';
  import { apiUrl, getCookie, setCookie } from '../utils.js'

  let user;
  async function refresh_token_auth(apiUrl, token, query) {
    const resp = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
        'HttpOnly': true
      },
      body: JSON.stringify({ query })
    });

    const { data } = await resp.json();
    if (resp.status == 200){
        setCookie('token', data.data.tokenAuth.token, true, 'Lax');
        setCookie('refresh-token', data.data.tokenAuth.refreshToken, true, 'Lax');
    }
    return data;
  }

  let token = getCookie('token');
  let refresh_token = getCookie('refreshtoken');

  onMount(async () => {
  if (refresh_token != null){
     let query = `mutation refreshToken{
        refreshToken(refreshToken:"${refresh_token}"){
            token
            refreshToken
        }
     }`
     let data = await refresh_token_auth(apiUrl, token, query)
  }
  })

  async function fetchUserData(apiUrl, token, query) {
    const resp = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
        'HttpOnly': true,
      },
      body: JSON.stringify({ query })
    });

    const { data } = await resp.json();
    return data.whoami;
  }

  if (token) {
      onMount(async () => {
          const query = '{whoami{id, username, email}}';
          user = await fetchUserData(apiUrl, token, query);
      });
  }
  else{
    window.location.href = '/#/login';
  }
</script>

{#if user}
  <p>Hello, {user.username}</p>
  <a href='/#/books'>Books</a>
{/if}
