<script>
  import jwt from 'jsonwebtoken';

  let username = '';
  let password = '';

  async function handleSubmit() {
    const apiUrl = 'http://localhost:8000/graphql/';
    const variables = { username, password};
    const query = `mutation TokenAuth($username: String!, $password: String!) {
        tokenAuth(username: $username, password: $password) {
            token
            payload
            refreshExpiresIn
        }
    }`
    const response = await fetch(apiUrl, {
      method: 'POST',
      body: JSON.stringify({ query, variables }),
      headers: { 'Content-Type': 'application/json' }
    });
    const data = await response.json();
    localStorage.setItem('token', data.token);
    const decodedToken = jwt.decode(data.token);
    console.log(decodedToken);
  }
</script>
<form on:submit={handleSubmit}>
  <label>
    Username:
    <input type="username" bind:value={username} />
  </label>
  <label>
    Password:
    <input type="password" bind:value={password} />
  </label>
  <button type="submit">Log in</button>
</form>

