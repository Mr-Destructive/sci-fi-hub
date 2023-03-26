  <div class="register-form">
    <h2>Register</h2>
    <form on:submit|preventDefault={handleRegister}>
      <label for="email">Email:</label>
      <input type="email" id="email" bind:value={email} />

      <label for="username">Username:</label>
      <input type="text" id="username" bind:value={username} />

      <label for="password">Password:</label>
      <input type="password" id="password" bind:value={password} />

      <button type="submit">Register</button>
    </form>
    <p>Already have an account? <a href='/#/login'>Login</a></p>

  </div>

<script>
  import { goto } from '@sapper/app';
  import { apiUrl } from '../utils';
  let email = '';
  let username = '';
  let password = '';

  async function handleRegister() {
    const query = `
      mutation CreateAuthor($email: String!, $username: String!, $password: String!) {
        createAuthor(email: $email, username: $username, password: $password) {
          token,
          refreshToken,
          author{
          id,
          username
          }
        }
      }
    `;
    const variables = { email, username, password };

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({query, variables})
      });

      if (!response.ok) {
        throw new Error('Registration failed');
      }else{
        //TODO: fix goto from sapper
        window.location.href = '/#/login';
      }
    } catch (error) {
      console.error(error);
    }
  }
</script>

