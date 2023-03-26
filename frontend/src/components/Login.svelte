  <div>
    <h1>Login</h1>
    <form on:submit|preventDefault="{handleSubmit}">
      <label>
        Username:
        <input type="text" bind:value="{username}">
      </label>
      <label>
        Password:
        <input type="password" bind:value="{password}">
      </label>
      <button type="submit">Submit</button>
    </form>
    Don't have a account <a href='/#/register'>Register</a>
  </div>

<script>
  import jwt_decode from "jwt-decode";
  import { apiUrl, setCookie } from "../utils.js"
  let username = '';
  let password = '';
  
  async function handleSubmit() {
    let query = `
      mutation TokenAuth($username: String!, $password: String!) {
        tokenAuth(username: $username, password: $password) {
          token
          refreshToken
        }
      }
    `;
    const variables = { username, password };
    
    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'HttpOnly': true,
        },
        body: JSON.stringify({ query, variables })
      });

      const data = await response.json();
      setCookie('token', data.data.tokenAuth.token, true, 'Lax');
      setCookie('refreshtoken', data.data.tokenAuth.refreshToken, true, 'Lax');
      let token = data.data.tokenAuth.token;
      var decoded = jwt_decode(token);
      if (token){
          window.location.href = '/';
      }
    } catch (error) {
      console.error(error);
    }
  }
</script>
