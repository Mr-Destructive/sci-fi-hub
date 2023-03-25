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
    Don't have a account <a href='/register'>Register</a>
  </div>

<script>

  import jwt_decode from "jwt-decode";
  let username = '';
  let password = '';
  export let apiUrl = 'http://localhost:8000/graphql/';
  
  async function handleSubmit() {
    let query = `
      mutation TokenAuth($username: String!, $password: String!) {
        tokenAuth(username: $username, password: $password) {
          token
        }
      }
    `;
    const variables = { username, password };
    
    try {
    console.log(apiUrl);
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query, variables })
      });

      const data = await response.json();
      localStorage.setItem('token', data.data.tokenAuth.token);
      console.log(data.data.tokenAuth.token)
      let token = data.data.tokenAuth.token;
      var decoded = jwt_decode(token);
      console.log(decoded);
      window.location.href = '/';
    } catch (error) {
      console.error(error);
    }
  }
</script>
